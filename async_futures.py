import time
import asyncio
from asyncio import Future

# ANSI colors
colors = (
    "\033[0m",   # End of color
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[34m",  # Blue
)


async def bar(future):
    print(colors[1] + "bar will sleep for 3 seconds" + colors[0])
    await asyncio.sleep(3)
    print(colors[1] + "bar resolving the future" + colors[0])
    future.done()
    future.set_result("future is resolved")


async def foo(future):
    print(colors[2] + "foo will await the future" + colors[0])
    await future
    print(colors[2] + "foo finds the future resolved" + colors[0])


async def main():
    future = Future()
    await asyncio.gather(foo(future), bar(future))


if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(colors[3] + f"Future Start Time: {start_time}\nFuture End Time: {end_time}\nFuture Execution Time: {execution_time:0.2f} seconds." + colors[0])
