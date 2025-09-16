# Flask REST API - User Management

A simple REST API built with Flask for managing user data. This project demonstrates fundamental API development concepts including CRUD operations, HTTP methods, status codes, and JSON handling.

## Features

- **Complete CRUD Operations**: Create, Read, Update, Delete users
- **RESTful Design**: Follows REST API conventions
- **JSON Support**: All data exchange in JSON format
- **Error Handling**: Proper HTTP status codes and error messages
- **Data Validation**: Input validation and duplicate prevention
- **In-Memory Storage**: Simple dictionary-based data storage

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/users` | Get all users |
| GET | `/users/<id>` | Get user by ID |
| POST | `/users` | Create new user |
| PUT | `/users/<id>` | Update user |
| DELETE | `/users/<id>` | Delete user |
| GET | `/health` | Health check |

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- Flask

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/flask-rest-api.git
   cd flask-rest-api
   ```

2. **Install Flask**
   ```bash
   pip install flask
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the API**
   - Base URL: `http://localhost:5000`
   - Health check: `http://localhost:5000/health`

## Usage Examples

### 1. Get All Users
```bash
curl -X GET http://localhost:5000/users
```

**Response:**
```json
{
  "status": "success",
  "data": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "created_at": "2024-01-15"
    }
  ],
  "count": 1
}
```

### 2. Get User by ID
```bash
curl -X GET http://localhost:5000/users/1
```

### 3. Create New User
```bash
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice Johnson", "email": "alice@example.com"}'
```

**Response:**
```json
{
  "status": "success",
  "message": "User created successfully",
  "data": {
    "id": 3,
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "created_at": "2024-09-16"
  }
}
```

### 4. Update User
```bash
curl -X PUT http://localhost:5000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "John Updated", "email": "john.updated@example.com"}'
```

### 5. Delete User
```bash
curl -X DELETE http://localhost:5000/users/1
```

## Testing with Postman

1. **Import Collection**: Create a new collection in Postman
2. **Set Base URL**: `http://localhost:5000`
3. **Test Each Endpoint**:
   - GET `/users` - No body required
   - POST `/users` - Set Content-Type to `application/json`, add body with name and email
   - PUT `/users/1` - Same as POST, but update existing user
   - DELETE `/users/1` - No body required

## HTTP Status Codes Used

- **200 OK**: Successful GET, PUT requests
- **201 Created**: Successful POST request
- **400 Bad Request**: Invalid JSON or missing required fields
- **404 Not Found**: User not found or invalid endpoint
- **405 Method Not Allowed**: Invalid HTTP method for endpoint
- **409 Conflict**: Email already exists

## Data Structure

### User Object
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2024-01-15"
}
```

### API Response Format
```json
{
  "status": "success|error",
  "message": "Description message",
  "data": "Actual data object/array",
  "count": "Number of items (for lists)"
}
```

## Key Concepts Demonstrated

1. **REST Architecture**: Resource-based URLs, HTTP methods
2. **Flask Routing**: Different routes for different operations
3. **JSON Handling**: `request.get_json()` and `jsonify()`
4. **HTTP Methods**: GET, POST, PUT, DELETE
5. **Status Codes**: Appropriate codes for different scenarios
6. **Error Handling**: Try-catch blocks and error responses
7. **Data Validation**: Required field checking, duplicate prevention
8. **In-Memory Storage**: List and dictionary data structures

## Interview Questions Covered

1. **What is Flask?** - Lightweight Python web framework
2. **What is REST?** - Representational State Transfer architectural style
3. **GET vs POST?** - GET retrieves data, POST creates data
4. **Flask Routes** - `@app.route()` decorator maps URLs to functions
5. **request.json** - Accesses JSON data from HTTP request body
6. **Status Codes** - 200 (success), 404 (not found), 201 (created), etc.
7. **Running Flask** - `python app.py` or `flask run`
8. **JSON** - JavaScript Object Notation, lightweight data format
9. **API Testing** - Using curl, Postman, or browser dev tools
10. **Database Alternative** - Yes, can use SQLite, PostgreSQL, MongoDB instead of in-memory storage

## Future Enhancements

- Add database integration (SQLite/PostgreSQL)
- Implement authentication and authorization
- Add input sanitization and validation
- Include pagination for large datasets
- Add logging and monitoring
- Create unit tests

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

---

**Author**: [Your Name]  
**Date**: September 2024  
**Purpose**: Flask REST API learning project
