# 这里是混合，两个并行任务，一个依赖任务
import asyncio
from delay_sleep import delay

async def hello_every_second():
    for i in range(2):
        await asyncio.sleep(1)
        print(f'i running other code while i am await')

async def main():
    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(3))

    await hello_every_second()
    await first_delay
    await second_delay

asyncio.run(main())
