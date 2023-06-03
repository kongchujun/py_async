# 取消任务很简单， 关键是什么时候调用取消方法以及如何监控
import asyncio
from asyncio import CancelledError
from delay_sleep import delay

async def main():
    long_task = asyncio.create_task(delay(10))
    seconds_elapsed=0
    while not long_task.done():
        print(f'任务没有完成， 每秒钟检查一次')
        await asyncio.sleep(1)
        seconds_elapsed = seconds_elapsed +1
        if seconds_elapsed == 5:
            long_task.cancel()
    
    try:
        await long_task
    except CancelledError:
        print('我们的任务取消了')

asyncio.run(main())