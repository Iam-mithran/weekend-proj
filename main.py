#Testing a line added
#uvicorn main:app --reload
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="/code")

#path based routing
@app.get("/")
def form_post(request: Request):
    return templates.TemplateResponse('form.html', context={'request': request})
