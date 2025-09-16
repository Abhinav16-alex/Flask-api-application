from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# In-memory storage for users (using a list of dictionaries)
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "created_at": "2024-01-15"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "created_at": "2024-01-16"}
]

# Helper function to find user by ID
def find_user_by_id(user_id):
    return next((user for user in users if user["id"] == user_id), None)

# Helper function to generate new ID
def generate_new_id():
    return max([user["id"] for user in users], default=0) + 1

# GET /users - Retrieve all users
@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify({
        "status": "success",
        "data": users,
        "count": len(users)
    }), 200

# GET /users/<id> - Retrieve a specific user
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = find_user_by_id(user_id)
    if user:
        return jsonify({
            "status": "success",
            "data": user
        }), 200
    else:
        return jsonify({
            "status": "error",
            "message": "User not found"
        }), 404

# POST /users - Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate required fields
        if not data or 'name' not in data or 'email' not in data:
            return jsonify({
                "status": "error",
                "message": "Missing required fields: name and email"
            }), 400
        
        # Check if email already exists
        if any(user['email'] == data['email'] for user in users):
            return jsonify({
                "status": "error",
                "message": "Email already exists"
            }), 409
        
        # Create new user
        new_user = {
            "id": generate_new_id(),
            "name": data['name'],
            "email": data['email'],
            "created_at": datetime.now().strftime("%Y-%m-%d")
        }
        
        users.append(new_user)
        
        return jsonify({
            "status": "success",
            "message": "User created successfully",
            "data": new_user
        }), 201
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "Invalid JSON data"
        }), 400

# PUT /users/<id> - Update a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        user = find_user_by_id(user_id)
        if not user:
            return jsonify({
                "status": "error",
                "message": "User not found"
            }), 404
        
        data = request.get_json()
        if not data:
            return jsonify({
                "status": "error",
                "message": "No data provided"
            }), 400
        
        # Check if email already exists (excluding current user)
        if 'email' in data:
            if any(u['email'] == data['email'] and u['id'] != user_id for u in users):
                return jsonify({
                    "status": "error",
                    "message": "Email already exists"
                }), 409
        
        # Update user fields
        if 'name' in data:
            user['name'] = data['name']
        if 'email' in data:
            user['email'] = data['email']
        
        return jsonify({
            "status": "success",
            "message": "User updated successfully",
            "data": user
        }), 200
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "Invalid JSON data"
        }), 400

# DELETE /users/<id> - Delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = find_user_by_id(user_id)
    if not user:
        return jsonify({
            "status": "error",
            "message": "User not found"
        }), 404
    
    users.remove(user)
    return jsonify({
        "status": "success",
        "message": "User deleted successfully"
    }), 200

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "message": "Flask REST API is running"
    }), 200

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "status": "error",
        "message": "Endpoint not found"
    }), 404

# Error handler for 405 (Method Not Allowed)
@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "status": "error",
        "message": "Method not allowed"
    }), 405

if __name__ == '__main__':
    print("Starting Flask REST API...")
    print("Available endpoints:")
    print("GET    /users       - Get all users")
    print("GET    /users/<id>  - Get user by ID")
    print("POST   /users       - Create new user")
    print("PUT    /users/<id>  - Update user")
    print("DELETE /users/<id>  - Delete user")
    print("GET    /health      - Health check")
    app.run(debug=True, host='0.0.0.0', port=5000)
