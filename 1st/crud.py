from sqlalchemy.orm import Session
from models import Status, Task
from schemas import StatusCreate, TaskCreate

# Status CRUD
def create_status(db: Session, status: StatusCreate):
    db_status = Status(name=status.name)
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status

def get_statuses(db: Session):
    return db.query(Status).all()


# Task CRUD
def create_task(db: Session, task: TaskCreate):
    db_task = Task(title=task.title, description=task.description, status_id=task.status_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session, status_id: int = None):
    query = db.query(Task)
    if status_id:
        query = query.filter(Task.status_id == status_id)
    return query.all()

def update_task(db: Session, task_id: int, title: str, description: str, status_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.title = title
        task.description = description
        task.status_id = status_id
        db.commit()
        db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task
