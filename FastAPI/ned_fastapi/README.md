`poetry add fastapi uvicorn httpie httpx requests`

step 1: create `main.py` file in the subfolder

```
from fastapi import FastAPI

app: FastAPI = FastAPI()


@app.get('/')
def index():
    return {"Hello": "World"}
    
    
```


Running Poetry Project:

`poetry run uvicorn ned_fastapi.main:app --reload`  

# Mock Server or Auto Documentation of your Application

'http://localhost:8000/docs'

References:

* https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
* https://fastapi.tiangolo.com/tutorial/first-steps/


Synchronous Functions:
Synchronous functions execute sequentially, meaning the program waits for each function to complete before proceeding to the next line of code.

Asynchronous Functions:
Asynchronous functions allow the program to continue executing other tasks while waiting for the function to complete.
