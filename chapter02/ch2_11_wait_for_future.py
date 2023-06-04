from asyncio import Future
import asyncio

async def set_future_value(future)->None:
    await asyncio.sleep(1)
    future.set_result(48)

def make_resquest() -> Future:
    future = Future()
    asyncio.create_task(set_future_value(future))
    return future

async def main():
    future = make_resquest()
    print(f'is future is done? {future.done()}')
    value = await future
    print(f'is future is done? {future.done()}')
    print(value)

asyncio.run(main())
