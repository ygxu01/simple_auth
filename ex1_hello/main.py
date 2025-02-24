from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount the "main" directory to serve static files
app.mount("/", StaticFiles(directory="main", html=True), name="main")

# Don't use this for Vercel: This is just for demo purposes
# If you use the code below, then run it with `python main.py`
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
