# 使用装饰器并行两个任务， 两个任务时间密集型任务
import sys
sys.path.append('/Users/kcj/projects/py_project/py_async')

import asyncio
from util.async_timer import async_time
# from util.delay_sleep import delay

@async_time()
async def delay(delay_seconds: int) -> int:
    print(f'sleeping for {delay_seconds} seconds')
    await asyncio.sleep(delay_seconds)
    print(f'finished sleeping for {delay_seconds} seconds')
    return delay_seconds

@async_time()
async def main():
    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(3))

    await task_one
    await task_two

asyncio.run(main())

