import uvicorn
from fastapi import FastAPI


# Create the FastAPI app
app = FastAPI()


# Create the routes
@app.get("/")
async def root():
    """Default route, returns a JSON object with a message."""
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def hello(name: str):
    """/hello route. Returns a JSON object with a message containing the name."""
    return {"message": f"Hello {name}"}


# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
