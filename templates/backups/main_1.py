# Import our python modules needed for NoSQL db (Mongo) and Flask for the GUI
from flask import Flask, render_template, request, redirect
from flask import jsonify
from bson import json_util
from pymongo import MongoClient

# Create the 'app' object
host = 'localhost'
port = 5000
app = Flask(__name__)

# Connect to MongoDB
mongo_uri = 'mongodb://localhost:27017/'
client = MongoClient(mongo_uri)
db = client['Datastream_db']
collection = db['Data_collection']


# Create dummy data for a retail store
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

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Retrieve the data from the form
        new_data = {
            "_id": str(uuid.uuid4()),  # Generate a new UUID for the _id field
            "item": request.form['item'],
            "price": float(request.form['price']),
            "quantity": int(request.form['quantity']),
            "category": request.form['category'],
            "brand": request.form['brand'],
            "color": request.form['color'],
            "size": request.form['size'],
            "material": request.form['material']
        }

        # Check if the data is already in the collection
        existing_data = collection.find_one({"_id": new_data["_id"]})

        if existing_data:
            # Data is already in the collection, do nothing
            return redirect('/')
        else:
            # Data is not in the collection, insert it
            collection.insert_one(new_data)

        # Redirect to the display page
        return redirect('/')
    else:
        # Render the form template
        return render_template('add.html')


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        # Retrieve the updated data from the form
        updated_data = {
            "item": request.form['item'],
            "price": float(request.form['price']),
            "quantity": int(request.form['quantity']),
            "category": request.form['category'],
            "brand": request.form['brand'],
            "color": request.form['color'],
            "size": request.form['size'],
            "material": request.form['material']
        }

        # Update the data in the collection
        collection.update_one({'_id': id}, {'$set': updated_data})

        # Redirect to the display page
        return redirect('/')
    else:
        # Retrieve the data to be edited
        data = collection.find_one({'_id': id})

        # Render the form template with the data
        return render_template('edit.html', data=data)

@app.route('/remove/<id>')
def remove(id):
    # Remove the data from the collection
    collection.delete_one({'_id': id})

    # Redirect to the display page
    return redirect('/')

@app.route('/rename_field', methods=['GET', 'POST'])
def rename_field():
    if request.method == 'POST':
        # Retrieve the field to be renamed and the new name
        old_name = request.form['old_name']
        new_name = request.form['new_name']

        # Rename the field in all documents in the collection
        collection.update_many({}, {'$rename': {old_name: new_name}})

        # Redirect to the display page
        return redirect('/')
    else:
        # Render the form template
        return render_template('rename.html')


@app.route('/add_field', methods=['GET', 'POST'])
def add_field():
    if request.method == 'POST':
        # Retrieve the field name and default value
        field_name = request.form['field_name']
        default_value = request.form['default_value']

        # Add the field to all documents in the collection
        collection.update_many({}, {'$set': {field_name: default_value}})

        # Redirect to the display page
        return redirect('/')
    else:
        return render_template('add_field.html')


@app.route('/merge_fields', methods=['GET', 'POST'])
def merge_fields():
    if request.method == 'POST':
        # Retrieve the field names to be merged and the new field name
        field1_name = request.form['field1_name']
        field2_name = request.form['field2_name']
        new_field_name = request.form['new_field_name']

        # Merge the fields in all documents in the collection
        collection.update_many({}, {'$set': {new_field_name: {'$concat': ['$' + field1_name, ' ', '$' + field2_name]}}})
        collection.update_many({}, {'$unset': {field1_name: "", field2_name: ""}})

        # Redirect to the display page
        return redirect('/')
    else:
        # Display the merge fields form
        return render_template('merge_fields.html')


@app.route('/conditional_update', methods=['GET', 'POST'])
def conditional_update():
    if request.method == 'POST':
        # Retrieve the field name and condition
        field_name = request.form['field_name']
        condition = request.form['condition']
        new_value = request.form['new_value']

        # Update the data in the collection based on the condition
        collection.update_many({condition: {'$exists': True}}, {'$set': {field_name: new_value}})

        # Redirect to the display page
        return redirect('/')
    else:
        # Display the conditional update form
        return render_template('conditional_update.html')
    

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
