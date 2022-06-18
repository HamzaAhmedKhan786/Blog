from fastapi import FastAPI

app = FastAPI()

items = {
    "Blog_1": {
        "Blog_Id": 1,
        "Title": "SQLAlchemy 1.4.36 Released",
        "Availability": "SQLAlchemy 1.4.36 is now available.", 
        "Description": "Release 1.4.36 includes a variety of bugfixes, including one recent ORM related regression, as well as a memory leak issue in the now - deprecated C extensions that had gone unnoticed for many years, triggered by interpreting a Row object as a NumPy array among other cases involving fetching of non - present attributes ",
        "Date": "April 26, 2022",
        "Author": "Mike" },
    "Blog_2": {
        "Blog_Id": 2,
        "Title": "SQLAlchemy 1.4.37 Released",
        "Availability": "SQLAlchemy 1.4.37 is now available.", 
        "Description": "Release 1.4.37 includes a variety of bugfixes, including one recent ORM related regression, as well as a memory leak issue in the now - deprecated C extensions that had gone unnoticed for many years, triggered by interpreting a Row object as a NumPy array among other cases involving fetching of non - present attributes ",
        "Date": "April 27, 2022",
        "Author": "ARK" },
    "Blog_3": {
        "Blog_Id": 3,
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
async def create_item(mainName, Blog_Id, Title, Availability, Description, Date, Author):
    items = {mainName: {"name": Blog_Id, "Title": Title, "Availability": Availability, "Description": Description, "Date": Date, "Author": Author}}
    return items




    
# create blog, update blog, delete blog