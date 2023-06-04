import sys
sys.path.append('/Users/kcj/projects/py_project/py_async')

# 由于requsts库是阻塞的， 所以会阻塞任何线程，以后用aiohttp
import asyncio
from util import async_time
import requests

@async_time()
async def get_example_status()->int:
    return requests.get('https://www.baidu.com/').status_code


@async_time()
async def main():
    task1 = asyncio.create_task(get_example_status())
    task2 = asyncio.create_task(get_example_status())
    task3 = asyncio.create_task(get_example_status())

    await task1
    await task2
    await task3

asyncio.run(main())
