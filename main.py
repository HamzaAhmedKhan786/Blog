from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import uuid
app = FastAPI()

class ItemIn(BaseModel):
    Title: str
    Availability: str | None = None
    Description: str | None = None
    Date: str
    Author: str

class ItemOut(BaseModel):
    blog_id: str
    Title: str
    Availability: str | None = None
    Description: str | None = None
    Date: str
    Author: str

items = {
    "0": {
        "Title": "SQLAlchemy 1.4.36 Released",
        "Availability": "SQLAlchemy 1.4.36 is now available.", 
        "Description": "Release 1.4.36 includes a variety of bugfixes, including one recent ORM related regression, as well as a memory leak issue in the now - deprecated C extensions that had gone unnoticed for many years, triggered by interpreting a Row object as a NumPy array among other cases involving fetching of non - present attributes ",
        "Date": "April 26, 2022",
        "Author": "Mike" },
    "1": {
        "Title": "SQLAlchemy 1.4.37 Released",
        "Availability": "SQLAlchemy 1.4.37 is now available.", 
        "Description": "Release 1.4.37 includes a variety of bugfixes, including one recent ORM related regression, as well as a memory leak issue in the now - deprecated C extensions that had gone unnoticed for many years, triggered by interpreting a Row object as a NumPy array among other cases involving fetching of non - present attributes ",
        "Date": "April 27, 2022",
        "Author": "ARK"} ,
    "2": {
        "Title": "SQLAlchemy 1.4.38 Released",
        "Availability": "SQLAlchemy 1.4.38 is now available.", 
        "Description": "Release 1.4.38 includes a variety of bugfixes, including one recent ORM related regression, as well as a memory leak issue in the now - deprecated C extensions that had gone unnoticed for many years, triggered by interpreting a Row object as a NumPy array among other cases involving fetching of non - present attributes ",
        "Date": "April 28, 2022",
        "Author": "HAK" }
}

@app.get("/")
async def root():
    return {"message": "My Blog"}

@app.get("/items/")
async def read_item():
    return items

@app.post("/items/")
async def create_item(item: ItemOut):
    unique_id = str(uuid.uuid1())[:5]
    items[unique_id] = item.dict()
    return unique_id

@app.patch("/items/")
async def update_item(Blog_Id: str, item: ItemOut):
    stored_item_data = items[Blog_Id]
    stored_item_model = ItemOut(**stored_item_data)
    # item(**stored_item_data) == item(title="abc",Availability="xyz", Description="123")
    update_data = item.dict()
    updated_item = stored_item_model.copy(update=update_data)
    items[Blog_Id] = jsonable_encoder(updated_item)
    return updated_item

    
# create blog, update blog, delete blog