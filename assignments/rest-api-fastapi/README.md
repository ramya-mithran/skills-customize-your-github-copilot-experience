# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern REST APIs using the FastAPI framework. You'll create endpoints, handle path and query parameters, process request bodies, and implement proper response models using Python type hints.

## 📝 Tasks

### 🛠️ Create a Todo Management API

#### Description

Build a simple Todo management REST API with FastAPI that allows users to create, read, update, and delete todo items. Implement proper request validation, response models, and HTTP status codes. The API should store todos in memory and handle multiple operations efficiently.

#### Requirements

Completed API should:

- Define a Todo model with fields: id, title, description, completed (boolean), and created_at
- Implement GET /todos endpoint to retrieve all todos
- Implement POST /todos endpoint to create a new todo with request body validation
- Implement GET /todos/{todo_id} endpoint to retrieve a specific todo by ID
- Implement PUT /todos/{todo_id} endpoint to update an existing todo
- Implement DELETE /todos/{todo_id} endpoint to delete a todo
- Return appropriate HTTP status codes (200, 201, 404, 422 for validation errors)
- Use Pydantic models for request/response validation
- Include proper error handling and response messages
