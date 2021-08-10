import asyncio
import random
import time
from threading import Thread
from threading import current_thread

# ANSI colors
colors = (
    "\033[0m",   # End of color
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[34m",  # Blue
)


async def do_something_important(sleep_for):
    print(colors[1] + f"Is event loop running in thread {current_thread().getName()} = {asyncio.get_event_loop().is_running()}" + colors[0])
    await asyncio.sleep(sleep_for)


def launch_event_loops():
    # get a new event loop
    loop = asyncio.new_event_loop()

    # set the event loop for the current thread
    asyncio.set_event_loop(loop)

    # run a coroutine on the event loop
    loop.run_until_complete(do_something_important(random.randint(1, 5)))

    # remember to close the loop
    loop.close()


if __name__ == "__main__":
    thread_1 = Thread(target=launch_event_loops)
    thread_2 = Thread(target=launch_event_loops)

    start_time = time.perf_counter()
    thread_1.start()
    thread_2.start()

    print(colors[2] + f"Is event loop running in thread {current_thread().getName()} = {asyncio.get_event_loop().is_running()}" + colors[0])

    thread_1.join()
    thread_2.join()
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(colors[3] + f"Event Loop Start Time: {start_time}\nEvent Loop End Time: {end_time}\nEvent Loop Execution Time: {execution_time:0.2f} seconds." + colors[0])
