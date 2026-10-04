from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from train import model

app = FastAPI()

# Mount static files folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup Jinja2 templates (folder name must match your project directory)
templates = Jinja2Templates(directory="template")


class Data(BaseModel):
    text: str


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
def prediction(data: Data):
    raw_pred = model.predict([data.text])[0]
    return {
        "text": data.text,
        "prediction": str(raw_pred)
    }
