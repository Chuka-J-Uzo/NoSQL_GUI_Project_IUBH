


# MongoDB document databases provide high availability and easy scalability.

Our python version is '''3.10.6'''

OS

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
       
	  ```python -m pip install "pymongo[gssapi,aws,ocsp,snappy,zstd,encryption]"```


### Docker install a Mongo image
	docker pull mongo

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
