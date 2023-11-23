import pymongo

url = "mongodb+srv://tusharpanumatcha:qBbnPqu8Br51xhLG@cluster0.naqsaxb.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(url)
db = client['Research-pal']
mainDb = client['Research_Pal']
