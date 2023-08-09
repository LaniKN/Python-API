from flask import Flask, request, jsonify

app = Flask(__name__)
'''
@app.route("/")
def home():
    return "Home"
'''
## HTTP methods
'''
GET: request data
POST: Create a Resource
PUT: Update a resource
DELETE: Delete a Resource
'''

@app.route("/get-user/<user_id>")
def get_user(user_id):
    ##means you can get smth and / any value you want. the value will be the ID of the user
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    
    


if __name__ == "__main__":
    app.run(debug=True)

