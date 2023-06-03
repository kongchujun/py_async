# 利用线程的fib，比较上次的的时间结果， 证明在cpu密集型中，
# 线程对提高效率是没有太大的作用的， 而且只有遇到IO的时候
# GIL才会解锁
import time
import threading

def print_fib(number:int) -> None:
    def fib(n:int) -> int:
        if n==1:
            return 0
        elif n==2:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    print(f'fib({number}) is {fib(number)}')

def fib_with_threads():
    number_40_thread = threading.Thread(target=print_fib, args=(40,))
    number_41_thread = threading.Thread(target=print_fib, args=(41,))

    number_40_thread.start()
    number_41_thread.start()

    number_40_thread.join()
    number_41_thread.join()

start_threads = time.time()

fib_with_threads()

end_threads = time.time()
# 04的时间完全一样， 设置更多， 这就是CPU密集型的问题， 多线程的价值被完全否定
print(f'完成时间为 {end_threads - start_threads:.4f} 秒')