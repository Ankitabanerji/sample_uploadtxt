import pymongo

client = pymongo.MongoClient()
db = client.test

print(db)


def upload_data_mongo():
    d = {
        "name": "Ankita",
        "surname": "Banerji",
        "email": "ankitajhumu@gmail.com"
    }

    db1 = client['mongotest']
    coll = db1['test']
    coll.insert_one(d)

    record = coll.find()
    for i in record:
        print(i)
