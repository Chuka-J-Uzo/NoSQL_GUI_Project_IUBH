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


store_data = [
    {"item": "Item 1", "price": 14.6, "quantity": 50, "category": "Category 1", "brand": "Brand Gaeger", "color": "Red", "size": "Small", "material": "Cotton"},
    {"item": "Item 2", "price": 70.2, "quantity": 30, "category": "Category 2", "brand": "Brand Umlaut", "color": "Blue", "size": "Medium", "material": "Polyester"},

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


@app.route('/remove_field', methods=['POST'])
def remove_field():
    # Retrieve the field to be removed
    field_name = request.form['field_name']

    # Remove the field from all documents in the collection
    collection.update_many({}, {'$unset': {field_name: 1}})

    # Redirect to the display page
    return redirect('/')


@app.route('/rename_field', methods=['POST'])
def rename_field():
    # Retrieve the field to be renamed and the new name
    old_name = request.form['old_name']
    new_name = request.form['new_name']

    # Rename the field in all documents in the collection
    collection.update_many({}, {'$rename': {old_name: new_name}})

    # Redirect to the display page
    return redirect('/')


@app.route('/add_field', methods=['POST'])
def add_field():
    # Retrieve the field name and default value
    field_name = request.form['field_name']
    default_value = request.form['default_value']

    # Add the field to all documents in the collection
    collection.update_many({}, {'$set': {field_name: default_value}})

    # Redirect to the display page
    return redirect('/')


@app.route('/merge_fields', methods=['POST'])
def merge_fields():
    # Retrieve the names of the two fields to be merged and the name of the new merged field
    field1 = request.form['field1']
    field2 = request.form['field2']
    new_field = request.form['new_field']

    # Merge the two fields in all documents in the collection
    collection.update_many({}, {'$set': {new_field: {'$concat': ['$' + field1, ' ', '$' + field2]}}})

    # Remove the original fields from all documents in the collection
    collection.update_many({}, {'$unset': {field1: 1, field2: 1}})

    # Redirect to the display page
    return redirect('/')

@app.route('/display')
def display():
    # Retrieve data from the database
    store_data = collection.find()

    # Convert the cursor to a list
    items = list(store_data)

    # Convert ObjectId to string format
    for item in items:
        item['_id'] = str(item['_id'])

    # Render the data in the template
    return render_template('display.html', items=items)



if __name__ == '__main__':
    app.run(host, port, debug=True)
