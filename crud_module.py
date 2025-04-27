#!/usr/bin/env python
# coding: utf-8

# In[68]:


from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB"""
    
    def __init__(self):
        #Initializing the MongoClient. This helps to
        #access the MongoDB databases and collections. 
        #This is hard-wired to use the aac database, the 
        # animals collection, and the aac user. 
        # Definitions of the connection string variables are 
        # unique to the individual Apporto environment.
        # 
        # You must edit the connection variables below to reflect 
        # your own instance of MongoDB!
        #
        # Connection Variables 
        # 
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 34275
        DB = 'aac'
        COL = 'animals'
        # 
        # Initialize Connection
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
    #Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            # validating that data is a dictionary
            try:
                self.database.animals.insert_one(data) # data should be dictionary
                return True # Return True to indicate successful insert
            except Exception as e: 
                print(f"Error inserting document: {e}") #Print error message in case of failure
                return False # Return False if there is an error
        else:
            raise Exception("Nothing to save, because data parameter is empty")
                        
        #Create method to implement the R in CRUD.
        
    def read(self, query):
            """Query documents from the specified MongoDB collection"""
            try: 
                results = self.collection.find(query) # Use find() for querying 
                return list(results) # Convert the cursor to a list 
            except Exception as e: 
                print(f"Error querying documents: {e}")
                return[] # Return an empty list if there's an error
            
       # update multiple documents in the collection
    def update(self, query, update_data):
    
        if query is None or update_data is None: # Validate parameters
            raise ValueError ("Both query and update_data parameters are required")
        try:
            #update_many() affects all matching documents, #selection criteria, Update operator
            result = self.collection.update_many(query,{'$set': update_data})
            return result.modified_count # Return modification count
        except Exception as e: 
            print(f"Error updating documents: {e}")
            return 0 #Zero indicate no modifications
  
            
    def delete(self, query):
        """ Delete documents from the collection"""
       
        if query is None: 
            raise ValueError ("Query parameter required for deletion")
            try:
                #delete_many() removes all matching documents
                result = self.collection.delete_many(query)
                return result.deleted_count # Return deletion count 
            except Exception as e: 
                print(f"Deletion failed: {e}")
                return 0 # Zero indicates no deletions 
    # Custom helper queries
    def water_rescue(self):
        return self.read({
            "breed": {"$in": ["Labrador Retriever Mix", "Chesapeake Bay Retriever", "Newfoundland"]},
            "sex_upon_outcome": "Intact Female",
            "age_upon_outcome_in_weeks": {"$gte": 26, "$lte": 156}
        })

    def mountain_rescue(self):
        return self.read({
            "breed": {"$in": ["German Shepherd", "Alaskan Malamute", "Old English Sheepdog", "Siberian Husky", "Rottweiler"]},
            "sex_upon_outcome": "Intact Male",
            "age_upon_outcome_in_weeks": {"$gte": 26, "$lte": 156}
        })

    def disaster_rescue(self):
        return self.read({
            "breed": {"$in": ["Doberman Pinscher", "German Shepherd", "Golden Retriever", "Bloodhound", "Rottweiler"]},
            "sex_upon_outcome": "Intact Male",
            "age_upon_outcome_in_weeks": {"$gte": 20, "$lte": 300}
        })        
    
                
# In[ ]:




