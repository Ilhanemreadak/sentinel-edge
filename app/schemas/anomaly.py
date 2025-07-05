from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Any

class Anomaly(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    event_time: datetime
    event_type: str
    payload: Any

