from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
import logging
from app.core.database import get_session
from app.schemas.anomaly import Anomaly
from app.core.models import anomaly as anomaly_table  # Aşağıda oluşturacağız

router = APIRouter()
logger = logging.getLogger("uvicorn.error")

@router.get("/health", tags=["monitoring"])
async def health():
    return {"status": "ok"}

@router.get("/anomalies", response_model=List[Anomaly], tags=["anomaly"])
async def list_anomalies(limit: int = 100, db: AsyncSession = Depends(get_session)):
    try:
        result = await db.execute(
            select(
                anomaly_table.c.event_time,
                anomaly_table.c.event_type,
                anomaly_table.c.payload
            )
            .order_by(anomaly_table.c.event_time.desc())
            .limit(limit)
        )
        rows = result.all()
        return [
            {"event_time": r.event_time, "event_type": r.event_type, "payload": r.payload}
            for r in rows
        ]
    except Exception as e:
        # Bu logger, uvicorn.error kanalına yazar
        import logging
        logger = logging.getLogger("uvicorn.error")
        logger.exception("Error while fetching anomalies")
        # Client’a basit bir 500 mesajı gönderelim
        from fastapi import HTTPException
        raise HTTPException(status_code=500, detail="Internal server error")