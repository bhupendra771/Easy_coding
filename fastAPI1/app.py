import imp
from fastapi import FastAPI
import uvicorn

app = FastAPI()

usernames = list()
@app.get("/")
def home():
    return "Hello World"

@app.get("/home/{user_name}")
def get_data(user_name):
    return {
        "User_name":user_name
    }

@app.put("/put_data/{user_name}")
def put_data(user_name):
    usernames.append(user_name)
    print(usernames)
    return {
        "user_name":user_name
    }
@app.post("/post_data/{user_name}")
def post_data(user_name):
    usernames.append(user_name)
    return{
        "username":usernames
    }

@app.delete("/delete_data/{user_name}")
def delete_user(user_name):
    usernames.remove(user_name)
    return {
        "username":usernames
    }
    

if __name__ == "__main__":
    uvicorn.run(app)