import time


def count():
    print("One", end=" ")
    time.sleep(1)
    print("Two", end=" ")
    time.sleep(2)
    print("Three", end=" ")


def main():
    for _ in range(5):
        count()


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"\nExecuting - {__file__}\nExecution Starts: {start_time}\nExecutions Ends: {end_time}\nTotals Execution Time:{execution_time:0.2f} seconds.")
