import json

database = {"models": []}

def save_database():
    with open('models_database.json', 'w') as json_file:
        json.dump(database, json_file)

def load_database():
    global database
    try:
        with open('models_database.json', 'r') as json_file:
            database = json.load(json_file)
    except FileNotFoundError:
        save_database()

def register_model(model_id, initial_balance):
    database["models"].append({"id": model_id, "balance": initial_balance, "penalties": 0})
    save_database()

def deposit_funds(model_id, amount):
    for model in database["models"]:
        if model["id"] == model_id:
            model["balance"] += amount
            save_database()
            return True
    return False

def apply_penalty(model_id, penalty_amount):
    for model in database["models"]:
        if model["id"] == model_id:
            model["balance"] -= penalty_amount
            model["penalties"] += 1
            save_database()
            return True
    return False

load_database()