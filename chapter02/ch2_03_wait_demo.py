import asyncio

async def hello_message() ->str:
    await asyncio.sleep(1)
    return 'hello world'

async def main()->None:
    message = await hello_message()
    print(message)
    
asyncio.run(main())