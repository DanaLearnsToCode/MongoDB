import pymongo
import os
import sys
import pprint

post =  {"name": "bob",
         "Age": "36",
         "height": "5'11""}        

          

def main():
    connection_string = os.environ["MONGO_CONNECTION_STRING"]
    db_name = os.environ["MONGO_DBNAME"]
    
    client = pymongo.MongoClient(connection_string)
    db = client[db_name]
    collection = db['LearningClusters'] #1. put the name of your collection in the quotes
    
    #2. add a document to your collection using the insert_one method

    collection.insert_one(post)
   
         
         


    #3. print the number of documents in the collection
    print(collection.count())
    
    #4. print the first document in the collection
    print(collection.findOne())
    #5. print all documents in the collection
    
    #6. print all documents with a particular value for some attribute
    #ex. print all documents with the birth date 12/1/1990
    
    
if __name__=="__main__":
    main()
