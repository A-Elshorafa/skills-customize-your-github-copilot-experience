# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI and practice core backend skills such as routing, request validation, status codes, and CRUD operations.

## 📝 Tasks

### 🛠️ Create Your First API Endpoints

#### Description
Set up a FastAPI application and create basic routes to verify your API is running.

#### Requirements
Completed program should:

- Create a `FastAPI` app instance.
- Add a `GET /` endpoint that returns a welcome JSON message.
- Add a `GET /health` endpoint that returns API status information.


### 🛠️ Build Item CRUD Endpoints

#### Description
Use an in-memory data structure to manage a list of items with create, read, update, and delete functionality.

#### Requirements
Completed program should:

- Define a data model using Pydantic (for example: `name`, `price`, `in_stock`).
- Add `POST /items` to create an item.
- Add `GET /items` and `GET /items/{item_id}` to read items.
- Add `PUT /items/{item_id}` to update an item.
- Add `DELETE /items/{item_id}` to remove an item.
- Return proper status codes for success and not-found cases.


### 🛠️ Add Query Parameters and Validation

#### Description
Improve your API with filtering and data validation so clients can request exactly what they need.

#### Requirements
Completed program should:

- Add optional query parameters to `GET /items` (for example: `min_price`, `in_stock_only`, `limit`).
- Validate inputs using type hints and Pydantic constraints.
- Return clear error responses when validation fails.
- Keep endpoint behavior consistent and predictable.
