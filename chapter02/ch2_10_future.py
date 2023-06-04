# 展示了future的作用， 只有在赋值的之后，才是true


from asyncio import Future

my_future = Future()

print(f'is my furture done?{my_future.done()}')

my_future.set_result(42)
print(f'is my furture done?{my_future.done()}')
print(f'what is the result of my future?{my_future.result()}')
