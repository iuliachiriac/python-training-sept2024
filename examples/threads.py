import threading
import time


def func(nr):
    # print("from inside", threads)
    time.sleep(3)
    print(f"Finished execution from thread {nr}")


time_start = time.time()
threads = set()
print(f"No. of threads before starting any threads: {threading.active_count()}")

for i in range(1, 6):
    t = threading.Thread(target=func, args=(i,))
    threads.add(t)
    t.start()  # target(*args) / func(i)

    print(f'Thread {t.name} alive status: {t.is_alive()}')

    count = threading.active_count()
    print(f"Total no of threads: {count}")

for thread in threads:
    thread.join()

time_end = time.time()
total_time = time_end - time_start
print(f'Total time: {total_time:.10f}')