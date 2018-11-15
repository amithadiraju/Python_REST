from flask import Flask, request
from flask_restful import Resource, Api

import firebase_admin

# For connecting to firestore database and authentication
from firebase_admin import credentials, firestore

# For Cross-Origin Http requests
from flask_cors import CORS, cross_origin

# For Data base Connectivity
from firebase_admin import db

from flask import jsonify

application = app = Flask(__name__)
api = Api(app)

#Initializing cross origin callable app
CORS(app)

#Changed this thing here
#Here are some more changes
# Imade lot of CHANGESIOVSBVSBVLESJVB
class Firebase_Data(Resource):

    '''This class is used to connect to a firestore database and fetch the data from it.
    
    We connect to the fire store database using a JSON file which contains important credentials ( which will be encrypted)
    
    we then fetch all the data from the database and only access the INCIDENT section of it. We then iterate over each record 
    
    and fetch the co-ordinates from them. '''

    def get(self):

        return self._getData()

    def _getData(self):

        ''' Private function to connect to fire store database'''

        # Setting up credentials to connect.
        '''Please replace the arguments to the call to .Certificate method with the path of 
         ServiceAccountKey.JSON file. I had the file in the same directory. So, didn't include a PATH '''
        cred = credentials.Certificate(r'Cred.json')

        # Setting up secure connection to firestore Real time database

        Kokomo_app = firebase_admin.initialize_app(cred, {
            'projectId' : 'product-kokomo247'
        })


        # Connecting to the firestore client
        db_ref = firestore.client()

        # Referring to the 'Incident' section of the data
        ref_inc = db_ref.collection(u'incident')

        # Fetching all the records under that particular section and converting them to list of dictionaries
        docs = list( ref_inc.get() )

        

        lat_long = []

        # Iterating over each record inside the database
        for doc in docs:

            # Converting each document to a dictionary
            data = doc.to_dict()

            # Accessing the latitude and longitudes of each record and storing them to a list
            lat_long.append(
                
                { 'Latitude:' : data['latitude'], 'Longitude' : data['longitude'] } )

        # Returning a list of dictionaries
        return lat_long
    
# Add a URL where the data can be seen  
api.add_resource(Firebase_Data, '/Firebase_Data') # Route_1

if __name__ == '__main__':
     
     # Runs on port 5002 on any server
     app.run(port=5002)   
