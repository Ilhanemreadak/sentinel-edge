from sqlalchemy import Table, Column, BigInteger, Text, JSON, TIMESTAMP, MetaData

metadata = MetaData()

anomaly = Table(
    "anomaly",
    metadata,
    Column("event_time", TIMESTAMP(timezone=True), primary_key=True),
    Column("id", BigInteger, primary_key=True),
    Column("event_type", Text, nullable=False),
    Column("payload", JSON, nullable=False),
)