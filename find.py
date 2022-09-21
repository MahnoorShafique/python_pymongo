import pymongo


def hi():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    collection_ = mydb['mySampleCollection']

    # this will fetch random 1 document.
    one = collection_.find_one()
    print(one)

    # finding 1 particular  document
    one1=collection_.find_one({"name":"a"})
    print(one1)

    # all documents
    allDocs=collection_.find({"name":"d"})
    for i in allDocs:
        print("--",i)
    print("count at f=", collection_.count_documents({"name": "f"}))

    #limiting the record
    allDocs = collection_.find({}).limit(3)
    print(allDocs)
    for i in allDocs:
        print("only 3", i)



    # showing specific fields and hiding other
    #1---> to show
    #0--->hide
    # if we set 1 to a field all other fields will set to zero. vice versa
    #id is by default 1 ,you have to set it to 0 if you want to hide it.
    allDocs=collection_.find({"name":"d"},{"name":0})
    print("count=",collection_.count_documents({"name":"f"}))
    for i in allDocs:
        print("--",i)

    #using modifiers {gte,lte}
    #fetching those documents where age is  less than 24
    all_doc=collection_.find({"age":{"$lte":24}})
    print(all_doc)
    for item in all_doc:
        print(item)


if __name__ == '__main__':
    hi()
