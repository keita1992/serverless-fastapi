from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/articles", status_code=200)
async def root():
  return {"message": "Hello! This is a test API for serverless-fastapi app"}

handler = Mangum(app)