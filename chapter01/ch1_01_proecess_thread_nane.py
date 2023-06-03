import os
import threading

# 进程的信息在os的包中
print(f'当前进程的id: {os.getgid()}')

# 获取当前进程中活跃的线程数目
total_threads = threading.active_count()
# 获取当前线程的名称
thread_name = threading.current_thread().name

# 显示出来， 这个显示方法以前还是少用
print(f'当前运行的线程数目：{total_threads}')
print(f'当先线程的名字: {thread_name}')