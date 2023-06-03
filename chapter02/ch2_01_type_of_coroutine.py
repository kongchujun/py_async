async def coroutine_add_one(number:int)-> int:
    return number + 1

def add_one(number:int) ->int:
    return number + 1

funcation_result = add_one(1)
coroutine_result = coroutine_add_one(1)
# 不能直接运行coroutine
print(f'结果: {funcation_result}, 类型: {type(funcation_result)}')
print(f'结果: {coroutine_result}, 类型: {type(coroutine_result)}')