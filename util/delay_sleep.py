import asyncio

async def delay(delay_seconds:int) -> int:
    print(f'sleeping fro {delay_seconds} seconds')
    await asyncio.sleep(delay_seconds)
    print(f'finished sleeping for {delay_seconds} seconds')
    return delay_seconds

