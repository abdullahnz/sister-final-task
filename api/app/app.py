#!/usr/bin/python3

from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
from celery import Celery
import os
import uvicorn

BROKER_URL = os.getenv("BROKER_URL")
BACKEND_URL = os.getenv("BACKEND_URL")

celery = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Zip Cracker Parallel API"}

@app.post("/zipcrack")
async def zipcrack(zip_file: UploadFile):
    zip_path = f"uploads/{zip_file.filename}"
    
    with open(zip_path, "wb") as f:
        f.write(zip_file.file.read())
    
    task = celery.send_task("bruteforce", args=(zip_path, ))
    
    return {"task_id": task.id}
    

@app.get("/zipcrack/{task_id}")
async def status(task_id: str):
    result = celery.AsyncResult(task_id)
    
    password = result.get() if result.status == "SUCCESS" else None
    
    return {"task_id": task_id, "status": result.status, "result": password}
 
 
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)