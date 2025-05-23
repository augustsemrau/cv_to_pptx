from fastapi import FastAPI, Form, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

from .convert import convert
from .ppt_generator import json_to_ppt

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate")
def generate(cv_text: str = Form(...)):
    data = convert(cv_text)
    ppt_bytes = json_to_ppt(data)
    headers = {
        "Content-Disposition": "attachment; filename=cv.pptx"
    }
    return Response(content=ppt_bytes, media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation", headers=headers)
