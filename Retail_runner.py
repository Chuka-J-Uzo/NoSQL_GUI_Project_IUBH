# Import our python modules needed for NoSQL db (Mongo) and TKinter for the GUI
from flask import Flask, render_template, request, redirect
from tkinter import *
from tkinter import simpledialog
from pymongo import MongoClient
from pymongo.cursor import Cursor
from pymongo.server_api import ServerApi
import pprint
import io
import re
import sys


root = Tk()
root.title("Retail Inventory App - NoSQL DB - IUBH")
root.bell()

# Our sample database
store_data = [
    {"item": "Item 1 ", "price": 14.6, "quantity": 50, "category": "Category 1", "brand": "Brand Gaeger", "color": "Red", "size": "Small", "material": "Cotton"},
    {"item": "Item 2 🛍", "price": 70.2, "quantity": 30, "category": "Category 2", "brand": "Brand Umlaut", "color": "Blue", "size": "Medium", "material": "Polyester"}
]


# Connect to MongoDB
mongo_uri = 'mongodb://localhost:27017/'
client = MongoClient(mongo_uri)
db = client['Datastream_db']
collection = db['Data_collection']


# Set the Stable API version when creating a new client
client = MongoClient(mongo_uri, server_api=ServerApi('1'))
                          
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



# Insert the data into the collection
collection.insert_many(store_data)



# Define a list of auto-completion options
autocomplete_options = [
    'store_data',
    'collection.insert_one',
    'collection.insert_many',
    'collection.find',
    'collection.update_one',
    'collection.update_many',
    'collection.delete_one',
    'collection.delete_many',
    'collection.updateOne',
    'db.collection.updateOne',    
    'db.command'
]


# Create text input box
text_input = Text(root, width=60, height=2)
text_input.grid(row=0, column=0, padx=5, pady=5)

# Create button to execute code
def execute_code(event=None):
    code = text_input.get("1.0", END)
    buf = io.StringIO()

    try:
        # Check if the code contains MongoDB commands
        if re.search(r'\b(db\.[\w\.]+)\b', code):
            # Execute MongoDB commands and print the results
            result = db.command(code.strip())
            pprint.pprint(result, stream=buf)
        else:
            # Redirect stdout to buffer and evaluate Python code
            sys.stdout = buf
            result = eval(code)
            sys.stdout = sys.__stdout__

            # Check if the result is a cursor object and print each document
            if isinstance(result, Cursor):
                result = [doc for doc in result]
                for doc in result:
                    pprint.pprint(doc, stream=buf)
            else:
                pprint.pprint(result, stream=buf)

        # Display the results in the display_box
        display_box.insert(END, buf.getvalue())
        display_box.insert(END, "Code executed successfully!\n")

    except Exception as e:
        # Display any errors in the display_box
        display_box.insert(END, str(e))


# Bind Shift+Enter key to execute_code function
text_input.bind('<Shift-Return>', execute_code)

execute_button = Button(root, text="Execute", command=execute_code)
execute_button.grid(row=0, column=1, padx=5, pady=5)

# Create clear button
def clear_display():
    display_box.delete('1.0', END)

clear_button = Button(root, text="Clear", command=clear_display)
clear_button.grid(row=0, column=2, padx=5, pady=5)

# Create display box
display_box = Text(root, width=80, height=40)
display_box.grid(row=1, column=0, columnspan=2, padx=5, pady=5)


# Create auto-complete function
def autocomplete(event):
    text = event.widget.get("1.0", "end-1c")
    if text:
        matches = [option for option in autocomplete_options if option.startswith(text)]
        if len(matches) == 1:
            event.widget.delete("1.0", "end")
            event.widget.insert("1.0", matches[0])
        elif len(matches) > 1:
            selection = simpledialog.askstring("Autocomplete", "Did you mean one of these?\n" + "\n".join(matches))
            if selection:
                event.widget.delete("1.0", "end")
                event.widget.insert("1.0", selection)

# Bind auto-complete function to text input box
text_input.bind("<Tab>", autocomplete)


root.mainloop()

def execute_code(event=None):
    code = text_input.get("1.0", END)
    buf = io.StringIO()

    try:
        # Check if the code contains MongoDB commands
        if re.search(r'\b(db\.[\w\.]+)\b', code):
            # Execute MongoDB commands and print the results
            result = db.command(code.strip())
            pprint.pprint(result, stream=buf)
        else:
            # Redirect stdout to buffer and evaluate Python code
            sys.stdout = buf
            result = eval(code)
            sys.stdout = sys.__stdout__

            # Check if the result is a cursor object and print each document
            if isinstance(result, Cursor):
                result = [doc for doc in result]
                for doc in result:
                    pprint.pprint(doc, stream=buf)
            else:
                pprint.pprint(result, stream=buf)

        # Display the results in the display_box
        display_box.insert(END, buf.getvalue())

    except Exception as e:
        # Display any errors in the display_box
        display_box.insert(END, str(e))
