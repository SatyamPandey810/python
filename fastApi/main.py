from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def read_root():
    return 'hello world'


@app.get('/about')
def about():
    data={
        "name":"john doe",
        "age":10,

    }
    return data


# dynamic routing
@app.get('/home/{username}')
def home(username):
    return {
        "page":"home page",
        "username":username
    }
