from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from schemas import Status, StatusCreate, Task, TaskCreate
import crud

# Initialize database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Status Routes
@app.post("/statuses/", response_model=Status)
def create_status(status: StatusCreate, db: Session = Depends(get_db)):
    return crud.create_status(db=db, status=status)

@app.get("/statuses/", response_model=list[Status])
def get_statuses(db: Session = Depends(get_db)):
    return crud.get_statuses(db=db)

# Task Routes
@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    status = crud.create_task(db=db, task=task)
    if not status:
        raise HTTPException(status_code=400, detail="Invalid status_id")
    return status

@app.get("/tasks/", response_model=list[Task])
def get_tasks(status_id: int = None, db: Session = Depends(get_db)):
    return crud.get_tasks(db=db, status_id=status_id)

@app.put("/tasks/{task_id}/", response_model=Task)
def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    updated_task = crud.update_task(db=db, task_id=task_id, title=task.title, description=task.description, status_id=task.status_id)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@app.delete("/tasks/{task_id}/")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted_task = crud.delete_task(db=db, task_id=task_id)
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}
