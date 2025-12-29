from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import models
from database import engine
from routeres import auth, todos, admin, users


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory='./templates')
app.mount('/static', StaticFiles(directory='./static'), name='static')
# name='static' could be static2 or any name

@app.get('/')
def test(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)