import json, asyncio, os, random, datetime
from aiokafka import AIOKafkaProducer

KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "localhost:9092")
TOPIC = "hdfs-traces"


async def main():
    producer = AIOKafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
    await producer.start()
    try:
        while True:
            msg = {
                "timestamp": datetime.datetime.utcnow().isoformat(),
                "event_id": random.randint(1, 100),
                "message": "mock log line",
            }
            await producer.send_and_wait(TOPIC, msg)
            print("➡️  sent", msg)
            await asyncio.sleep(2)
    finally:
        await producer.stop()

if __name__ == "__main__":
    asyncio.run(main())
