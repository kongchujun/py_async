import sys
sys.path.append('/Users/kcj/projects/py_project/py_async')

import asyncio
from util.delay_sleep import delay
def call_later():
    print(f'in call of future')

async def main():
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(1)

asyncio.run(main())