from fastapi import FastAPI, BackgroundTasks
from models import ExecuteRequest
from executor import execute_task
from runtime_store import runtime_db

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/internal/execute")
async def execute(request: ExecuteRequest, background_tasks: BackgroundTasks):
    project_id = request.project_id

    runtime_db[project_id] = {
        "status": "running",
        "result": None
    }

    background_tasks.add_task(execute_task, request)

    return {"message": "Task started", "project_id": project_id}

@app.get("/runtime/{project_id}")
async def get_runtime(project_id: str):
    return runtime_db.get(project_id, {"error": "Not found"})
