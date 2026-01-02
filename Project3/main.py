from fastapi import FastAPI, Request, status
from fastapi.staticfiles import StaticFiles
import models
from database import engine
from routeres import auth, todos, admin, users
from fastapi.responses import RedirectResponse


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.mount('/static', StaticFiles(directory='./static'), name='static')
# name='static' could be static2 or any name

@app.get('/')
def test(request: Request):
    return RedirectResponse('/todos/todo-page', status_code=status.HTTP_302_FOUND)


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)