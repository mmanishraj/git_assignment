from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.todo_db
collection = db.items

@app.route('/submittodoitem', methods=['POST'])
def submit():
    data = {
        "name": request.form['itemName'],
        "description": request.form['itemDescription']
    }
    collection.insert_one(data)
    return "Item Saved"
