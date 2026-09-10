'''
While raw SQLite is suitable for smaller projects, SQLAlchemy is the standard industry-level ORM (Object Relational Mapping) tool used in production applications.
'''

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session

from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"

# Create Database Connection
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
    # Passing check_same_thread: False allows FastAPI to safely manage concurrent multi-threaded connections.
)

# To handle database operations and queries
sessionLocal = sessionmaker(bind=engine)

# Base declarative class serves as the parent class for all database models
Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id= Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(String)

Base.metadata.create_all(bind=engine)

# Helper function is created to supply an isolated database session for each incoming API request.
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create API
@app.post("/todos")
def create_todo(title:str, db: Session= Depends(get_db)):
    todo = Todo(title = title, completed = False)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        "message": "Todo created",
        "data": todo
    }

# Read all data
@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return{
        "total": len(todos),
        "data": todos
    }

# Read particular data
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int, db:Session=Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id==todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

# Update the data
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, title: str, db: Session=Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id==todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    todo.title = title
    db.commit()
    db.refresh(todo)

    return{
        "message": "Todo updated",
        "data": todo
    }

# Delete API
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session= Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id==todo_id).first()
    if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()

    return{
        "message": "Todo deleted",
        "data": todo
    }