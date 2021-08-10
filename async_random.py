import time
import asyncio
import random

# ANSI colors
colors = (
    "\033[0m",   # End of color
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[36m",  # Cyan
    "\033[35m",  # Magenta
    "\033[34m",  # Blue
)


async def generate_random_int(indx: int, threshold: int = 5) -> int:
    print(colors[indx + 1] + f"Initiated generate_random_int({indx}).")
    i = random.randint(0, 10)
    while i <= threshold:
        print(colors[indx + 1] + f"generate_random_int({indx}) == {i} too low; retrying.")
        await asyncio.sleep(indx + 1)
        i = random.randint(0, 10)
    print(colors[indx + 1] + f"---> Finished: generate_random_int({indx}) == {i}" + colors[0])
    return i


async def main():
    res = await asyncio.gather(*(generate_random_int(i, 10 - i - 1) for i in range(3)))
    return res


if __name__ == "__main__":
    random.seed(444)
    start_time = time.perf_counter()
    r1, r2, r3 = asyncio.run(main())
    print(colors[4] + f"\nRandom INT 1: {r1}, Random INT 2: {r2}, Random INT 3: {r3}\n" + colors[0])
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(colors[5] + f"Program Start Time: {start_time}\nProgram End Time: {end_time}\nProgram Execution Time: {execution_time:0.2f} seconds." + colors[0])
