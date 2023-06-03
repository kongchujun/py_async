# 这里才是真正的并行执行
# 1.被包裹的任务方法肯定是一个异步定义的方法
# 2.使用asyncio.create_task创建任务
# 3.使用await来触发任务，停止主线程， 然后子协程来执行后面的任务
import asyncio
import time
from delay_sleep import delay

async def main():
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(3))

    await sleep_for_three
    await sleep_again
    await sleep_once_more

start = time.time()
asyncio.run(main())
end = time.time()
print(f'{end - start:.4f}')