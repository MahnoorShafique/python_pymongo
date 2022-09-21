import pymongo


def print_hi():
    # client instance pointing to local db
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    #using mongodbdb atlas
    # myclient = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0.ruanruv.mongodb.net/?retryWrites=true&w=majority")
    # making a db reference
    mydb = myclient["mydatabase"]
    print(mydb)
    print("list all db names", myclient.list_database_names())
    # we won't be able to see database in mongo db compass until we create collection and insert data into collection.
    collection_ = mydb['mySampleCollection']
    print("collection object", mydb.list_collections())
    print("list all collection names", mydb.list_collection_names())

    # print(collection_)

    # insert one document:
    dictionry = {"name": "d", "age": 22, "phone": 9237654589274}
    collection_.insert_one(dictionry)

    # insert multiple documents:
    dict = [{"name": "e", "age": 22, "phone": 9237654589274},
            {"name": "f", "age": 23, "phone": 9237654589274},
            {"name": "g", "age": 24, "phone": 9237654589274},
            {"name": "h", "age": 25, "phone": 9237654589274},
            {"name": "i", "age": 26, "phone": 9237654589274}]
    collection_.insert_many(dict)


    #using my own id rather then auto id provided by db
    dict = [{"_id":1,"name": "e", "age": 22, "phone": 9237654589274},
            {"_id":2,"name": "f", "age": 23, "phone": 9237654589274},
            {"_id":3,"name": "g", "age": 24, "phone": 9237654589274},
            {"_id":4,"name": "h", "age": 25, "phone": 9237654589274},
            {"_id":5,"name": "i", "age": 26, "phone": 9237654589274}]
    collection_.insert_many(dict)


if __name__ == '__main__':
    print_hi()
