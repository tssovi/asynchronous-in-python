import asyncio
import time


async def count():
    print("One", end=" ")
    await asyncio.sleep(1)
    print("Two", end=" ")
    await asyncio.sleep(2)
    print("Three", end=" ")


async def main():
    await asyncio.gather(count(), count(), count(), count(), count())


if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"\nExecuting - {__file__}\nExecution Starts: {start_time}\nExecutions Ends: {end_time}\nTotals Execution Time:{execution_time:0.2f} seconds.")
