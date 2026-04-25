from fastapi import FastAPI, BackgroundTasks
from models import ExecuteRequest
from executor import execute_task
from runtime_store import runtime_db

print("Starting app...")

from fastapi import FastAPI, BackgroundTasks
print("FastAPI imported")

from models import ExecuteRequest
print("Models imported")

from executor import execute_task
print("Executor imported")

from runtime_store import runtime_db
print("Runtime store imported")

app = FastAPI()

# 🔥 Brain → Heart
@app.post("/internal/execute")
async def execute(request: ExecuteRequest, background_tasks: BackgroundTasks):
    project_id = request.project_id

    # Set initial state
    runtime_db[project_id] = {
        "status": "running",
        "result": None
    }

    # Run task in background
    background_tasks.add_task(execute_task, request)

    return {"message": "Task started", "project_id": project_id}


# 🔥 Frontend → Heart
@app.get("/runtime/{project_id}")
async def get_runtime(project_id: str):
    return runtime_db.get(project_id, {"error": "Not found"})
