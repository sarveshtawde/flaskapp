@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    data = request.json
    itemName = data.get("itemName")
    itemDescription = data.get("itemDescription")
    db.todos.insert_one({"name": itemName, "description": itemDescription})
    return {"message": "Item submitted"}
