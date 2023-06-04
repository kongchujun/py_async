import sys
sys.path.append('/Users/kcj/projects/py_project/py_async')

# 看cpu密集型的任务是无法处理的
import asyncio
from util.async_timer import async_time
# from util.delay_sleep import delay

@async_time()
async def cpu_bound_work()->int:
    counter = 0
    for i in range(100000000):
        counter = counter + 1
    return counter

@async_time()
async def main():
    task_one = asyncio.create_task(cpu_bound_work())
    await task_one

asyncio.run(main(),debug=True)