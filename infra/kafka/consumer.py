import json, asyncio, os, asyncpg
from aiokafka import AIOKafkaConsumer

# asyncpg yalnızca "postgresql://" veya "postgres://" şemasını kabul eder
DB_DSN = os.getenv(
   "DB_DSN", "postgresql://postgres:sentinel@localhost:5432/sentinel"
)
KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "localhost:9092")
TOPIC = "hdfs-traces"

INSERT_SQL = """
    INSERT INTO anomaly (event_time, event_type, payload)
    VALUES (NOW(), $1, $2::jsonb)
"""

async def main():
    pool = await asyncpg.create_pool(dsn=DB_DSN, min_size=1, max_size=5)
    consumer = AIOKafkaConsumer(
        TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP,
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="sentinel-edge-consumer",
    )
    await consumer.start()
    try:
        async for msg in consumer:
            data = msg.value
            async with pool.acquire() as conn:
                await conn.execute(INSERT_SQL, "hdfs-log", json.dumps(data))
            print("⬅️  stored", data)
    finally:
        await consumer.stop()
        await pool.close()

if __name__ == "__main__":
    asyncio.run(main())
