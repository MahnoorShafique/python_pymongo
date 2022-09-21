import pymongo

if __name__ == '__main__':
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    collection_ = mydb['mySampleCollection']

    #update one
    prev={"name":"a"}
    nextt={"$set":{"name":"A"}}
    collection_.update_one(prev,nextt)

    #update many
    prev = {"name": "d"}
    nextt = {"$set": {"name": "D"}}
    mod=collection_.update_many(prev, nextt)
    #checking how many records get modified
    print(mod.modified_count)

    #if it doesn't find the record to update it will insert as new entry
    #by setting {upsert:true}

    prev = {"name": "x"}
    nextt = {"$set": {"name": "upsertion "}}
    mod = collection_.update_many(prev, nextt,upsert=True)


    # increment operator

    # incrementing field for name:d to age+3
    mod1=collection_.update_one({"name":"g"},{"$inc":{"age":3}})
    print((mod1.modified_count))

    mod1 = collection_.update_many({"name": "g"}, {"$inc": {"age": 3}})
    print((mod1.modified_count))

    #renaming a field
    mod1 = collection_.update_many({"name": "g"}, {"$rename": {"name":"name_"}})
    print((mod1.modified_count))


