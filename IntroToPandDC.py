import threading
import time

# Worker function (used for both sequential and parallel)
def worker(worker_id, delay):
    print(f"Worker {worker_id} started (delay {delay}s)")
    time.sleep(delay)
    print(f"Worker {worker_id} finished")

# Sequential Execution Function
def run_sequential(num_workers, delay):
    print("\n--- Sequential Execution ---")
    start_time = time.time()

    for i in range(num_workers):
        worker(i, delay)

    end_time = time.time()
    print("All Workers Done (Sequential)")
    print(f"Sequential Time: {end_time - start_time:.2f} seconds")


# Parallel Execution Function
def run_parallel(delays):
    print("\n--- Parallel Execution (Multithreading) ---")
    start_time = time.time()

    threads = []

    for i in range(len(delays)):
        t = threading.Thread(target=worker, args=(i, delays[i]))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    end_time = time.time()
    print("All Workers Done (Parallel)")
    print(f"Parallel Time: {end_time - start_time:.2f} seconds")


# Main Program
if __name__ == "__main__":
    # Sequential: 4 workers with same delay
    run_sequential(num_workers=4, delay=2)

    # Parallel: 6 workers with different delays
    delays = [1, 2, 3, 1, 2, 3]
    run_parallel(delays)