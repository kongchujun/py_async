import sys
sys.path.append('/Users/kcj/projects/py_project/py_async')

# 其实加了sleep也无法使程序并行运行， cpu密集型就是这样， 遇到就不会跳出来的
import asyncio
from util.async_timer import async_time
from util.delay_sleep import delay

@async_time()
async def cpu_bound_work()->int:
    counter = 0
    for i in range(100000000):
        counter = counter + 1
    return counter

@async_time()
async def main():
    task_one = asyncio.create_task(cpu_bound_work())
    task_two = asyncio.create_task(cpu_bound_work())
    task_delay = asyncio.create_task(delay(2))

    await task_delay
    await task_one
    await task_two
   

asyncio.run(main())