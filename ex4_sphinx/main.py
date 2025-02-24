from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount the "main" directory to serve static files
app.mount("/", StaticFiles(directory="./ex4_sphinx/main", html=True), name="main")

# For this example, the vercel.json file should look like this:
"""
{
    "builds": [
        {
            "src": "ex4_sphinx/main.py",
            "use": "@vercel/python"
        }
    ],
    "routes": [
        {
            "src": "/(.*)",
            "dest": "ex4_sphinx/main.py"
        }
    ]
}  
"""