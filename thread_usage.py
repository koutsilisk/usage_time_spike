from multiprocessing import Process
from kmeans_usage import run
from time import thread_time, process_time


def start_4_threads():
    p1 = Process(run(400000, 4))
    p2 = Process(run(400000, 4))
    p3 = Process(run(400000, 4))
    p4 = Process(run(400000, 4))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()


def do_4_fn(fn):
    p1 = Process(start_4_threads())
    p2 = Process(start_4_threads())
    p3 = Process(start_4_threads())
    p4 = Process(start_4_threads())
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()


def time_multithreading(f, *param):
    t_start = process_time()
    if param:
        f(param)
    else:
        f()
    t_end = process_time()
    return t_end - t_start


if __name__ == "__main__":
    th_1_deep_time = time_multithreading(start_4_threads)
    print(f"----------- Thread execution time {th_1_deep_time}")

    th_2_deep_time = time_multithreading(do_4_fn, start_4_threads)
    print(f"-----------Thread execution time {th_2_deep_time}")
