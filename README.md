# DramatiqAckFailure
Dramatiq using the broker as rabbitmq is failing to acknowledge the message this the training occurs for same message again and again

## Prerequisites
- [x] Python3.x
    > Install the tqdm, dramatiq, pika packages
- [x] Docker
    > Runs the rabbitmq server


## Run RabbitMQ

```
# build the rabbitmq image
docker build -t rrabit -f Dockerfile .

# run the container
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rrabit
```

## Python consumer

```
virtualenv venv
source venv/bin/activate
pip install pika tqdm dramatiq
```

Run the consumer with the following command:
```
dramatiq worker --processes=1 --threads=1 --verbose
```

#### Looks for the exception at 60sec
```
[dramatiq.worker.ConsumerThread(test_queue)] [CRITICAL] Consumer encountered a connection error: (406, 'PRECONDITION_FAILED - consumer ack timed out on channel 1')
[dramatiq.worker.ConsumerThread(test_queue)] [INFO] Restarting consumer in 3.00 seconds.
```
