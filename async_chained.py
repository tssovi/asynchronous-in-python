import sys
import asyncio
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


async def function1(n: int) -> str:
    i = random.randint(0, 10)
    print(colors[1] + f"function1({n}) is sleeping for {i} seconds." + colors[0])
    await asyncio.sleep(i)
    result = f"result{n}-1"
    print(colors[1] + f"Returning function1({n}) == {result}." + colors[0])
    return result


async def function2(n: int, arg: str) -> str:
    i = random.randint(0, 10)
    print(colors[2] + f"function2{n, arg} is sleeping for {i} seconds." + colors[0])
    await asyncio.sleep(i)
    result = f"result{n}-2 derived from {arg}"
    print(colors[2] + f"Returning function2{n, arg} == {result}." + colors[0])
    return result


async def chain(n: int) -> None:
    start = time.perf_counter()
    p1 = await function1(n)
    p2 = await function2(n, p1)
    end = time.perf_counter() - start
    print(colors[3] + f"--> Chained result{n} => {p2} (took {end:0.2f} seconds)." + colors[0])


async def main(*args):
    await asyncio.gather(*(chain(n) for n in args))


if __name__ == "__main__":
    random.seed(444)
    args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
    start_time = time.perf_counter()
    asyncio.run(main(*args))
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(colors[4] + f"Program Start Time: {start_time}\nProgram End Time: {end_time}\nProgram Execution Time: {execution_time:0.2f} seconds." + colors[0])
