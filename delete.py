import pymongo

if __name__ == '__main__':
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    collection_ = mydb['mySampleCollection']

    #delete one
    docs={"name":"D"}
    collection_.delete_one(docs)

    #delete many
    docs = {"name": "D"}
    dele=collection_.delete_many(docs)
    print(dele.deleted_count)