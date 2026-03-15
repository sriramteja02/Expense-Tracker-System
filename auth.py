import bcrypt
import json

FILE = "users.json"

def load_users():
    try:
        with open(FILE) as f:
            return json.load(f)
    except:
        return {}

def save_users(users):

    with open(FILE,"w") as f:
        json.dump(users,f)

def register(username,password):

    users = load_users()

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    users[username] = hashed

    save_users(users)

def login(username,password):

    users = load_users()

    if username in users:

        if bcrypt.checkpw(password.encode(), users[username].encode()):
            return True

    return False