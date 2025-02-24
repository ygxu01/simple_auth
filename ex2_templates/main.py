from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates  
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")
message = "Hello class, from the .py file"

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": message})
