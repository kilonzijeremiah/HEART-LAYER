import time
from runtime_store import runtime_db

def execute_task(request):
    project_id = request.project_id

    try:
        time.sleep(3)

        result = {
            "message": f"Executed {request.task_type}",
            "data": request.payload
        }

        runtime_db[project_id] = {
            "status": "completed",
            "result": result
        }

    except Exception as e:
        runtime_db[project_id] = {
            "status": "failed",
            "error": str(e)
        }
