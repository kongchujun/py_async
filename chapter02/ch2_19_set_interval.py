import asyncio
# 可以手动设置超过的时间，如果任何协程占用CPU时间超过250毫米， 就会
# 收到信息
async def main():
    loop = asyncio.get_event_loop()
    loop.slow_callback_duration = .250

asyncio.run(main(), debug=True)