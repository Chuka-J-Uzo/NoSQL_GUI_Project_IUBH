## About this Application

This app is a solution for a small apparel retail store that needs to update prices of displayed items in response to the highly competitive pricing environment in its neighborhood.

`MongoDB` is the choice for this application because it is a highly scalable, document-oriented NoSQL database that can handle a large volume of data and provides flexible data modeling. It also allows for easy integration with other technologies, making it an ideal choice for modern web applications.

For quick data modelling and alterations to our database, we chose `MongoDB-Compass`. `MongoDB-Compass` is a GUI tool that provides a visual interface for managing and interacting with `MongoDB` databases, making it easier for users to navigate and work with the data.

We have also run this database on Docker in consideration of its advantages. Running `MongoDB` in a Docker container allows for easy deployment and management of the database, as well as providing a consistent and reproducible environment for the application. Containerization allows for better resource management and easier "horizontal" scaling of the application as the business grows.

The use of containerization also provides benefits such as improved portability, version control, and isolation, making it easier to maintain and deploy the application across different environments. 

Using `MongoDB`, `MongoDB Compass`, and Docker provides a modern and scalable solution for the apparel retail store's pricing update needs.


`MongoDB` document databases provide high availability and easy scalability.

### Our device Details

Our python version is `3.10.6`

Operating system is `Ubuntu 22.04 LTS`

### Files contained in our App directory

`main.py`: This is the main file for your Flask application. It contains the code for defining our Flask routes and handling HTTP requests and responses.

`README.md`: This is a markdown file that provides documentation and instructions on how to use the application.

`templates/`: This is a directory that contains the HTML templates for this application.

`docker-compose.yml`: This is a YAML config file that defines the MongoDB database container that should be run in our Docker environment.

`queries.md`: This is a markdown file that contains sample queries that can be run on our MongoDB database.

`requirements.txt`: This is a file that lists the Python packages that are required for our application to run. It contains some dependencies that pymongo requires to run.
## How to Use this Application:

### Install python client API for Mongo as well as Flask API
	pip install pymongo
	pip install flask

### Install dependencies
       sudo apt-get install libkrb5-dev
       
'''GSSAPI authentication requires pykerberos on Unix or WinKerberos on Windows. The correct dependency can be installed automatically along with PyMongo:'''
       
	   ```python3 -m pip install "pymongo[gssapi]"```
       
'''MONGODB-AWS authentication requires pymongo-auth-aws:'''
       
	   ```python3 -m pip install "pymongo[aws]"```
       
'''OCSP (Online Certificate Status Protocol) requires PyOpenSSL, requests, service_identity and may require certifi:'''       
       
	   ```python3 -m pip install "pymongo[ocsp]"```



'''Also you can just install all of them like this'''
       
	  ' python -m pip install "pymongo[gssapi,aws,ocsp,snappy,zstd,encryption]" '


### Docker install a Mongo image
	docker pull mongo

### Docker config for MongoDB

Included in the main directory is our `docker-compose.yml` file for those who prefer to build it that way.

The mongoDB docker image version looks like this:
      - "GOSU_VERSION=1.16"
      - "JSYAML_VERSION=3.13.1"
      - "MONGO_PACKAGE=mongodb-org"
      - "MONGO_REPO=repo.mongodb.org"
      - "MONGO_MAJOR=6.0"
      - "MONGO_VERSION=6.0.5"
      - "HOME=/data/db"


In our `docker-compose.yml` file, you will notice that we mounted the Database container on a volume to achieve "persistence" of the data to be written and manipulated on our container. 

Our volume details look like this:
	volumes:
		- "b4e8c304e3e0410b43f1acdaf13668c8e835fef15fd4300066e52eb17be4aedf:/data/configdb"
		- "3ac3575caa70f1b6b8bad599171a411b340ae490c932d1fcd2886268eb2a8800:/data/db"

### Start a mongo server instance
	docker run -d -p 27017:27017 --name mongodb mongo


'''After running the python app, if you need to run start the mongo daemon, 
enter the docker shell for the mongo container, then just type'''

        mongosh

### Create your mongodb using this link  https://www.mongodb.com/basics/create-database:

        use Datastream_db
        
### To manipulate our fields, we need MongoDB Compass

1. Download MongoDB Compass with: 
'wget https://downloads.mongodb.com/compass/mongodb-compass_1.35.0_amd64.deb'


2. Install MongoDB Compass:
	sudo dpkg -i mongodb-compass_1.35.0_amd64.deb
	
If you get an error with the above installation, then use this to fix any missing dependencies:
	sudo apt-get install -f
	
If it completes the fixing successfully, then proceed to retry: 
	sudo dpkg -i mongodb-compass_1.35.0_amd64.deb


3. Start MongoDB Compass:
	mongodb-compass


4. Once mongodb-compass GUI Interface is initialized, enter this command to switch to our database:
	use Datastream_db

5. Next, use the following commands to adjust or manipulate the fields accordingly:

### Delete a collection
        db.Data_collection.deleteMany({})
	
### Merge two fields
        db.Data_collection.updateMany({}, { $set: { merged_field: { $concat: ["$price", " ", "$quantity"] } } }, { multi: true })
### Rename a fields       
        db.Data_collection.updateOne({item: "Item 1"}, {$rename: {"category": "Category 1"}})
### Remove a field       
        db.Data_collection.updateOne({item: "Item 1"}, {$unset: {size: ""}})
### Add a field        
        db.Data_collection.updateOne({item: "Item 1"}, {$set: {"Size": "Medium"}})
        
### Do a conditional update for several fields
	db.Data_collection.updateMany(
  { category: "Category 1" },
  {
    $set: {
      price: { $multiply: ["$price", 1.1] },
      quantity: { $subtract: ["$quantity", 10] },
      brand: "New Brand"
    }
  }
)

     
### Add a field to a particular position
	       db.Data_collection.aggregate([
	  {
	    $match: { item: "Item 1" }
	  },
	  {
	    $addFields: {
	      Size: "Medium"
	    }
	  },
	  {
	    $project: {
	      _id: 0,
	      item: 1,
	      price: 1,
	      quantity: 1,
	      category: 1,
	      brand: 1,
	      color: 1,
	      Size: 1,
	      material: 1
	      
	    }
	  }
	])
