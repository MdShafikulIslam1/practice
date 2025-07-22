from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, FastAPI!"}

if __name__ == "__main__":
    uvicorn.run("app:app", host='0.0.0.0', port=8080, reload=True,log_level="debug")  # no reload here