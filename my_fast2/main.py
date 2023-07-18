from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


class ItemResponse(BaseModel):
    id: int
    name: str
    price: float


@app.post("/items", response_model=ItemResponse)
def create_item(item: Item = Body(...)) -> ItemResponse:
    """
    创建一个新的项目。

    - **name**: 项目名称
    - **price**: 项目价格

    返回创建的项目信息，包括生成的ID。
    """
    # 处理创建项目的逻辑
    # 返回ItemResponse对象作为响应
    item_id = 1  # 假设这是新项目的ID
    return ItemResponse(id=item_id, name=item.name, price=item.price)


@app.get("/items/{item_id}")
def get_item(item_id: int) -> ItemResponse:
    """
    获取项目信息。

    - **item_id**: 项目ID

    返回指定项目的详细信息。
    """
    # 处理获取项目信息的逻辑
    # 返回ItemResponse对象作为响应
    item = ItemResponse(id=item_id, name="Example Item", price=9.99)
    return item

