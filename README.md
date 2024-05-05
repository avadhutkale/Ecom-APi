
# RESTful API for Product Management

This project is a RESTful API built using the Flask web framework for managing products within an e-commerce application. It provides a set of endpoints to perform CRUD (GET, POST, PUT, DELETE) operations on product data stored in a SQLite database.


## Installation

1 Import the required libraries 

```
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

```
2 Create a Flask application

```
app = Flask(__name__)

```
3 Import SQLAlchemy and configure the database
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)

```
4 Define the Product model and create the database:
```
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    price = db.Column(db.Float, nullable=False)
db.create_all()

```
5 Implement the endpoints for CRUD operations
## Usage
1 Set the FLASK_APP environment variable:
```
set FLASK_APP=app.py

```
2 Run the Flask application:
```
flask run

```
3 Use Postman or any other API testing tool to send requests to the following endpoints:
```
GET: Display the list of products
URL: http://127.0.0.1:5000/products

POST: Add a new product
URL: http://127.0.0.1:5000/products
Body: JSON data of the product to be added

PUT: Update an existing product
URL: http://127.0.0.1:5000/products/<id>
Replace <id> with the ID of the product to be updated
Body: JSON data with the updated product information

DELETE: Delete a product
URL: http://127.0.0.1:5000/products/<id>
Replace <id> with the ID of the product to be deleted
```