"""
FastAPI Todo Management API - Starter Code

This is a starter template for building a REST API with FastAPI.
Follow the requirements in the README.md to complete the assignment.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uuid

# Initialize the FastAPI application
app = FastAPI(
    title="Todo Management API",
    description="A simple REST API for managing todo items",
    version="1.0.0"
)

# Define the Todo model using Pydantic for validation
class Todo(BaseModel):
    """Todo item model with validation"""
    title: str
    description: Optional[str] = None
    completed: bool = False

class TodoResponse(Todo):
    """Todo response model including id and created_at"""
    id: str
    created_at: datetime

# In-memory storage for todos (for this assignment, we'll use a dictionary)
todos_db: dict = {}

# TODO: Implement the following endpoints:
# 1. GET /todos - Retrieve all todos
# 2. POST /todos - Create a new todo
# 3. GET /todos/{todo_id} - Retrieve a specific todo
# 4. PUT /todos/{todo_id} - Update a todo
# 5. DELETE /todos/{todo_id} - Delete a todo

@app.get("/")
async def root():
    """Root endpoint - API is running"""
    return {"message": "Todo Management API is running"}

# Add your endpoint implementations below:
