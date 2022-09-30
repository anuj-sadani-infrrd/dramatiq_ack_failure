import time
import logging
import tqdm
import dramatiq
import pika
from dramatiq.brokers.rabbitmq import RabbitmqBroker

logger = logging.getLogger(__name__)

# rabbitmq_broker
credentials = pika.PlainCredentials("test", "test")
rabbitmq_broker = RabbitmqBroker(
    host="localhost",
    port="5672",
    virtual_host="/",
    heartbeat=30,
    credentials=credentials,
)
dramatiq.set_broker(rabbitmq_broker)


@dramatiq.actor(queue_name="test_queue", max_retries=0, time_limit=2400000)
def start_task(iters, msg):
    logger.info("msg: %s", msg)
    logger.info("#" * 88)
    for i in tqdm.tqdm(range(iters), position=0, leave=True):
        time.sleep(0.1)
    logger.info("Completed")
    logger.info("=" * 88)


# Sending a message to queue
logger.info("-" * 88)
logger.info(f"Sending iters")
time.sleep(1)
message = start_task.send(1000, {"msg": "some message"})
logger.info("Message send to queue successfully")
logger.info("-" * 88)
