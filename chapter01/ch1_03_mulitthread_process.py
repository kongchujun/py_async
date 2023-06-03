import multiprocessing
import os

def hello_from_process():
    print(f'hello从子进程{os.getgid()}')

if __name__== '__main__':
    hello_process = multiprocessing.Process(target=hello_from_process)
    hello_process.start()
    print(f'hello 从父母的进程 {os.getgid()}')
    hello_process.join()