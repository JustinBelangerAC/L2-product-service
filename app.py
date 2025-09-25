# I used chat gpt to convert from rust to python, the comments are mine
# import flask and cors
from flask import Flask, jsonify
from flask_cors import CORS

# import the env packages so that we can use env variables
from dotenv import load_dotenv
import os

# load the env vars
load_dotenv()

# create the flask obj
app = Flask(__name__)

# open cors on /products 
CORS(app, resources={r"/products": {"origins": "*"}}, methods=["GET"])

# define the /product route
@app.route("/products", methods=["GET"])
def get_products():

    # return a JSON array of the products
    return jsonify([
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99},
    ])

# the main function
if __name__ == "__main__":
    # get the port number from the env file / env var in azure
    port = int(os.getenv("PORT", 3030))

    # run the web app on the port we got from the env file
    app.run(host="0.0.0.0", port=port)
