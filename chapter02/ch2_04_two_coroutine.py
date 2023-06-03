# 由于都是协程，使用await的时候， main协程停止， 执行子协程
# 直到子协程执行完成， main协程才可以再启动
# 所有下面的任务逻辑，基本上跟sync没有任何区别
# 不同的是一维变二维, 只有通过任务才能实现并行
import asyncio
from delay_sleep import delay

async def add_one(number:int)->int:
    return number + 1

async def hello_world_msg() ->str:
    await delay(1)
    return 'hello world'

async def main() -> None:
    message = await hello_world_msg()
    one_plus_one = await add_one(1)
    print(one_plus_one)
    print(message)

asyncio.run(main())