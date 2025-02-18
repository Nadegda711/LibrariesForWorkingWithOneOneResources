from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
async def get_main_page() -> str:
    return "Главная страница"

@app.get("/user/admin")
async def get_admin_page() -> str:
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def get_user_number(user_id: int = Path(ge=0, le=100, description="Enter your id", example=77)) -> str:
    return f"Вы вошли как пользователь №{user_id}"

@app.get("/user/{username}/{age}")
async def get_user_info(
    username: str = Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser"),
    age: int = Path(ge=18, le=120, description="Enter age", example=20)
) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст {age}."