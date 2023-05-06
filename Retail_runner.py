# Import our python modules needed for NoSQL db (Mongo) and TKinter for the GUI
from tkinter import *
from pymongo import MongoClient
import pprint
import io
from flask import Flask, render_template, request, redirect

root = Tk()

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

# Create text input box
text_input = Text(root, width=60, height=2)
text_input.grid(row=0, column=0, padx=5, pady=5)

# Create button to execute code
def execute_code():
    code = text_input.get("1.0", END)
    buf = io.StringIO()
    result = eval(code)
    pprint.pprint(result, stream=buf)
    display_box.insert(END, buf.getvalue())


execute_button = Button(root, text="Execute", command=execute_code)
execute_button.grid(row=0, column=1, padx=5, pady=5)

# Create display box
display_box = Text(root, width=80, height=40)
display_box.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
