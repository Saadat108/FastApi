from fastapi import FastAPI, Path
from enum import Enum
from typing import Optional

app = FastAPI()

students = {
    1:{
        "name": "John",
        "age": 17,
        "class": "year 12"
    },
    2:{
        "name": "Josh",
        "age": 16,
        "class": "year 11"
    }
}

fake_items_db = [{"item_name": "Foo"},{"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/", description="this is our first route")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}", description="gets student by id")
def get_student(student_id: int ):
    return students[student_id]

@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip+limit]

@app.get("/items/{item_id}")
async def get_items(item_id: str, q:Optional[str]=None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
        # return {"item_id": item_id, "q": q}
    if not short:
        item.update(
                {
                    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam pellentesque libero eu."
                }
            )
    return item

@app.get("/users/{user_id}/items/{items_id}")
async def get_user_item(user_id: int, item_id: str, q: str | None = None, short :bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {
                "description:": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam pellentesque libero eu."
            }
        )
    return item

@app.get("/users")
async def list_users():
    return {"message": "list users route"}

@app.get("/users/me")
async def get_current_user():
    return {"message": "this is the current user"}

@app.get("/users/{user_id}")
async def list_users(user_id: str):
    return {"user_id": user_id}

class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"

@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "you are healthy"}
    
    if food_name.value == "fruits":
        return {"food_name": food_name, "message": "you are still healthy but like sweet things"}
    
    return {"foor_name": "food_name", food_name: "I like choco milk"}