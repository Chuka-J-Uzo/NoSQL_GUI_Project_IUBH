


# MongoDB document databases provide high availability and easy scalability.

Our python version is '''3.10.6'''

OS

### Install python client API for Mongo as well as Flask API
	pip install pymongo
	pip install flask

### Install dependencies
       sudo apt-get install libkrb5-dev
       
'''GSSAPI authentication requires pykerberos on Unix or WinKerberos on Windows. The correct dependency can be installed automatically along with PyMongo:'''
       python3 -m pip install "pymongo[gssapi]"
       
'''MONGODB-AWS authentication requires pymongo-auth-aws:'''
       python3 -m pip install "pymongo[aws]" 
       
'''OCSP (Online Certificate Status Protocol) requires PyOpenSSL, requests, service_identity and may require certifi:'''       
       python3 -m pip install "pymongo[ocsp]"



'''Also you can just install all of them like this'''
       python -m pip install "pymongo[gssapi,aws,ocsp,snappy,zstd,encryption]"


### Docker install a Mongo image
	docker pull mongo

### Start a mongo server instance
	docker run -d -p 27017:27017 --name mongodb mongo


'''After running the python app, if you need to run start the mongo daemon, 
enter the docker shell for the mongo container, then just type'''

        mongosh

### Create your mongodb using this link  https://www.mongodb.com/basics/create-database:

        use Datastream_db
