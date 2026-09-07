from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    title: str
    status: bool

# Create Todo Task
@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {
        "Message": "Task Created.",
        "ToDo": todo
    }

# Fetch Todo task
@app.get("/todos")
def fetch_todos():
    return todos

# Fetch particular Todo task by task id
@app.get("/todos/{todo_id}")
def fetch_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"error":"Todo not found!"}

# Update Todo task (by task id)
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return{
                "message": "Todo updated!",
                "data": updated_todo
            }
    return{
        "error": "Todo not found!"
    }

# Delete a Todo task
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return{
                "message": "Data Deleted!"
            }
    return {
        "error":"Todo not found!"
    }
