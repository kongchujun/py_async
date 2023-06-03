# 其实就是通过shield来隐藏， 并且在except中， 是继续
# 而不是重新开始
import asyncio
from delay_sleep import delay

async def main():
    task = asyncio.create_task(delay(10))
    try:
        result = await asyncio.wait_for(asyncio.shield(task),5)
        print(result)
    except TimeoutError:
        print("take longer than 5 scondes, it will finish soon")
        result = await task
        print(result)

asyncio.run(main())