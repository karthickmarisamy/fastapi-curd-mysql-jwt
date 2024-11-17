from fastapi import FastAPI, Depends
from routers import query

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("Starting up the fastApi application")

@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down the FastApi application")
    
app.include_router(query.router)