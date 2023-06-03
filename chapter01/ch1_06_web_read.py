import time
import requests

def read_example() ->None:
    respones = requests.get("https://www.youtube.com")
    print(respones.status_code)

sync_start = time.time()

read_example()
read_example()

sync_end = time.time()

print(f'没有线程的情况下: {sync_end - sync_start:.4f} 秒')