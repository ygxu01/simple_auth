from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount the static files directory
app.mount("/", StaticFiles(directory="./ex3_vercel_simple/main", html=True), name="main")

# Don't use this for Vercel
# You don't need this because Vercel will run the app using
# the edge function, not uvicorn. This is configured in the
# vercel.json file.
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)


# The vercel.json file is used to configure the Vercel app. 
# It tells Vercel to run the app using the edge function, 
# not uvicorn. This is because the edge function is faster 
# and more efficient than uvicorn.
# The edge function is a function that is executed on the 
# edge, which is a fast and efficient way to run the app.
# It should look like this:
"""
{
    "builds": [
        {
            "src": "ex3_vercel_simple/main.py",
            "use": "@vercel/python"
        }
    ],
    "routes": [
        {
            "src": "/(.*)",
            "dest": "ex3_vercel_simple/main.py"
        }
    ]
}
"""