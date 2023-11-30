#!/usr/bin/python3

from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from tasks.zipcracker_tasks import bruteforce
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Zip Cracker Parallel API"}

@app.post("/zipcrack")
async def zipcrack(zip_file: UploadFile):
    zip_path = f"/tmp/{zip_file.filename}"
    
    with open(zip_path, "wb") as f:
        f.write(zip_file.file.read())
    
    task = bruteforce.delay(zip_path)
    
    return {"task_id": task.id}

@app.get("/zipcrack/{task_id}")
async def status(task_id: str):
    result = bruteforce.AsyncResult(task_id)
    
    password = result.get() if result.status == "SUCCESS" else None
    
    return {"task_id": task_id, "status": result.status, "result": password}
 
 
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)