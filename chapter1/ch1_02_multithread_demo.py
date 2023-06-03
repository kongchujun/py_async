import threading

def hello_from_thread():
    print(f'hello 从当前的线程 {threading.current_thread()}')

# 把方法塞入进程配置中， 然后让一个线程去跑它，使用start触发
hello_thread = threading.Thread(target=hello_from_thread)
hello_thread.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name

# -----只有一个线程， 估计是python版本相关导致的
print(f'当前python运行的线程数目: {total_threads}')
print(f'当前线程的名字:{thread_name}')

# join让程序停止,如果没有join, 后面前面的打印方法无法执行
# 其作用是等待线程完成，类似于go的waitgroup
hello_thread.join()