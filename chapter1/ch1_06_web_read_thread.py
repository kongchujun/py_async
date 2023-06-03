import time
import requests
import threading

def read_example() ->None:
    respones = requests.get("https://www.youtube.com")
    print(respones.status_code)

thread1 = threading.Thread(target=read_example)
thread2 = threading.Thread(target=read_example)

sync_start = time.time()

thread1.start()
thread2.start()

print("所有线程开始跑了")

thread1.join()
thread2.join()


sync_end = time.time()

print(f'没有线程的情况下: {sync_end - sync_start:.4f} 秒')