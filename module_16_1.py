from fastapi import FastAPI

app = FastAPI()

@ app.get("/")
async def welcome():
    return  {"Главная страница"}

@ app.get("/user/admin")
async def news():
    return  {"Вы вошли, как администратор"}

@ app.get("/user")
async def user_paginator(username: str, age: int) -> dict:
    return  {"Информация о пользователе. Имя": username, "Возраст": age}

# Информация о пользователе. Имя: <username>, Возраст: <age>

@ app.get("/user/{user_id}")
async def read(user_id: int):
    return  {f"Вы вошли как пользователь №{user_id}"}

