# 如何使用超时控制对协程进行限制
import asyncio
from delay_sleep import delay

async def main():
    delay_task = asyncio.create_task(delay(2))
    # await delay_task
    try:
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result) # 不会被触发， 它等不到
    except asyncio.exceptions.TimeoutError:
        print('got a timeout')
        print(f'was the task cancelled?{delay_task.cancelled()}')

asyncio.run(main())