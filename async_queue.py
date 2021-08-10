import asyncio
import argparse
import itertools as it
import os
import random
import time

# ANSI colors
colors = (
    "\033[0m",   # End of color
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[36m",  # Cyan
    "\033[34m",  # Blue
)


async def generate_item(size: int = 5) -> str:
    return os.urandom(size).hex()


async def random_sleep(caller=None) -> None:
    i = random.randint(0, 10)
    if caller:
        print(colors[1] + f"{caller} sleeping for {i} seconds." + colors[0])
    await asyncio.sleep(i)


async def produce(name: int, producer_queue: asyncio.Queue) -> None:
    n = random.randint(0, 10)
    for _ in it.repeat(None, n):  # Synchronous loop for each single producer
        await random_sleep(caller=f"Producer {name}")
        i = await generate_item()
        t = time.perf_counter()
        await producer_queue.put((i, t))
        print(colors[2] + f"Producer {name} added <{i}> to queue." + colors[0])


async def consume(name: int, consumer_queue: asyncio.Queue) -> None:
    while True:
        await random_sleep(caller=f"Consumer {name}")
        i, t = await consumer_queue.get()
        now = time.perf_counter()
        print(colors[3] + f"Consumer {name} got element <{i}>" f" in {now - t:0.5f} seconds." + colors[0])
        consumer_queue.task_done()


async def main(no_producer: int, no_consumer: int):
    q = asyncio.Queue()
    producers = [asyncio.create_task(produce(n, q)) for n in range(no_producer)]
    consumers = [asyncio.create_task(consume(n, q)) for n in range(no_consumer)]
    await asyncio.gather(*producers)
    await q.join()  # Implicitly awaits consumers, too
    for consumer in consumers:
        consumer.cancel()


if __name__ == "__main__":
    random.seed(444)
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--no_producer", type=int, default=10)
    parser.add_argument("-c", "--no_consumer", type=int, default=15)
    ns = parser.parse_args()
    start_time = time.perf_counter()
    asyncio.run(main(**ns.__dict__))
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(colors[4] + f"Program Start Time: {start_time}\nProgram End Time: {end_time}\nProgram Execution Time: {execution_time:0.2f} seconds." + colors[0])
