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
   
  
#using Postman to test API
#URL: http://127.0.0.1:5000/create-user
@app.route("/create-user", methods=["POST"])#if you also want to accept a GET request, you would put it with POST
def create_user():
  #  if request.method == "POST"#only do this for multiple methods
    global data
    data = request.get_json()
    #will give json data passed in body of request
    return jsonify(data), 201#second number is status request, could do smth more to add to database


 ## the URL: http://127.0.0.1:5000/get-user/123?extra="hello"

@app.route("/get-user/<user_id>")
def get_user(user_id):
    ##means you can get smth and / any value you want. the value will be the ID of the user
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com",
       # "userName": data
       #for userName: data, make sure you create the data value after initializing your server. So you have to request the POST for the data-
       # before you can GET it.
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    
    return jsonify(user_data), 200



if __name__ == "__main__":
    app.run(debug=True)

