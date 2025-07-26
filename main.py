from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from pydantic import BaseModel
from datetime import date, datetime
from typing import List, Optional
import json
import os

app = FastAPI(title="Personal Todo App", version="1.0.0")

# Setup templates
templates = Jinja2Templates(directory="templates")

# Todo Model
class Todo(BaseModel):
    id: int
    task: str
    due: date

class TodoCreate(BaseModel):
    task: str
    due: date

class TodoUpdate(BaseModel):
    task: Optional[str] = None
    due: Optional[date] = None

# In-memory storage (ในการใช้งานจริงควรใช้ database)
todos: List[Todo] = []
next_id = 1

# Helper function to save/load data (optional persistence)
def load_todos():
    global todos, next_id
    if os.path.exists("todos.json"):
        try:
            with open("todos.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                todos = [Todo(**todo) for todo in data.get("todos", [])]
                next_id = data.get("next_id", 1)
        except:
            todos = []
            next_id = 1

def save_todos():
    data = {
        "todos": [todo.dict() for todo in todos],
        "next_id": next_id
    }
    with open("todos.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, default=str, indent=2)

# Load todos on startup
load_todos()

# Routes

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """หน้าแรกของ Web App"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/todos", response_model=List[Todo])
async def get_all_todos():
    """แสดง Todo ทั้งหมด (GET)"""
    return todos

@app.get("/todos/upcoming", response_model=List[Todo])
async def get_upcoming_todos():
    """แสดงเฉพาะงานที่ยังไม่ครบกำหนด (GET /todos/upcoming)"""
    today = date.today()
    upcoming = [todo for todo in todos if todo.due >= today]
    # เรียงลำดับตาม due date
    upcoming.sort(key=lambda x: x.due)
    return upcoming

@app.post("/todos", response_model=Todo)
async def create_todo(todo: TodoCreate):
    """เพิ่ม Todo ใหม่ พร้อม due date (POST)"""
    global next_id
    new_todo = Todo(
        id=next_id,
        task=todo.task,
        due=todo.due
    )
    todos.append(new_todo)
    next_id += 1
    save_todos()
    return new_todo

@app.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, todo_update: TodoUpdate):
    """แก้ไข Todo (PUT)"""
    # ค้นหา todo ที่ต้องการแก้ไข
    todo_index = None
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todo_index = i
            break
    
    if todo_index is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    # อัปเดตข้อมูล
    existing_todo = todos[todo_index]
    if todo_update.task is not None:
        existing_todo.task = todo_update.task
    if todo_update.due is not None:
        existing_todo.due = todo_update.due
    
    save_todos()
    return existing_todo

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    """ลบ Todo (DELETE)"""
    global todos
    original_length = len(todos)
    todos = [todo for todo in todos if todo.id != todo_id]
    
    if len(todos) == original_length:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    save_todos()
    return {"message": f"Todo {todo_id} deleted successfully"}

@app.get("/todos/{todo_id}", response_model=Todo)
async def get_todo(todo_id: int):
    """ดูรายละเอียด Todo เฉพาะ ID"""
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# Health check
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "total_todos": len(todos),
        "upcoming_todos": len([t for t in todos if t.due >= date.today()])
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)