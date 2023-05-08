# Import our python modules needed for NoSQL db (Mongo) and Flask for the GUI
from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

# Create the 'app' object
host = 'localhost'
port = 5000
app = Flask(__name__)

# Create the 'app' object
app = Flask(__name__)

# Connect to MongoDB
mongo_uri = 'mongodb://localhost:27017/'
client = MongoClient(mongo_uri)
db = client['Datastream_db']
collection = db['Data_collection']

# Our sample database
store_data = [
    {"item": "Item 1 ", "price": 14.6, "quantity": 50, "category": "Category 1", "brand": "Brand Gaeger", "color": "Red", "size": "Small", "material": "Cotton"},
    {"item": "Item 2 🛍", "price": 70.2, "quantity": 30, "category": "Category 2", "brand": "Brand Umlaut", "color": "Blue", "size": "Medium", "material": "Polyester"},
    {"item": "Item 3 🛍", "price": 130.7, "quantity": 20, "category": "Category 3", "brand": "Brand Caela", "color": "Green", "size": "Large", "material": "Silk"},
    {"item": "Item 4 🛍" , "price": 43.5, "quantity": 15, "category": "Category 1", "brand": "Brand Devon", "color": "Yellow", "size": "Small", "material": "Wool"},
    {"item": "Item 5 🛍", "price": 62.32, "quantity": 10, "category": "Category 2", "brand": "Brand Easel", "color": "Orange", "size": "Medium", "material": "Cotton"},
    {"item": "Item 6", "price": 60.0, "quantity": 5, "category": "Category 3", "brand": "Brand Flourish", "color": "Purple", "size": "Large", "material": "Polyester"},
    {"item": "Item 7", "price": 110.9, "quantity": 2, "category": "Category 1", "brand": "Brand Gourman", "color": "Black", "size": "Small", "material": "Leather"},
    {"item": "Item 8", "price": 80.3, "quantity": 1, "category": "Category 2", "brand": "Brand Heissen", "color": "White", "size": "Medium", "material": "Nylon"},
    {"item": "Item 9", "price": 90.05, "quantity": 0, "category": "Category 3", "brand": "Brand Texas", "color": "Brown", "size": "Large", "material": "Denim"},
    {"item": "Item 10", "price": 10.60, "quantity": 0, "category": "Category 1", "brand": "Brand Johannsen", "color": "Gray", "size": "Small", "material": "Polyester"}
]

# Insert the data into the collection
collection.insert_many(store_data)



# Define routes
@app.route('/')
def index():
    # Retrieve all data from the collection
    store_data = collection.find()

    # Convert the cursor to a list
    items = list(store_data)

    # Render the data in the template
    return render_template('index.html', items=items)


@app.route('/display')
def display():
    # Retrieve data from the database
    store_data = list(db.Data_collection.find())

    # Convert the cursor to a list
    items = list(store_data)

    # Convert ObjectId to string format
    for item in items:
        item['_id'] = str(item['_id'])

    # Render the data in the template
    return render_template('index.html', items=items)


if __name__ == '__main__':
    app.run(host, port, debug=True)
