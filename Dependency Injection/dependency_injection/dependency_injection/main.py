from fastapi import FastAPI, Depends, Query

from typing import Any, Annotated

app = FastAPI()

users: list[dict[Any, Any]] = [{'name':'mahpara', 'password':'777'},
{'name':'xyz', 'password':'123'},
{'name':'abc', 'password':'567'}
]

# The dependency function:
def user_dep(name: str = Query(...), password: str = Query(...)):
    for d in users:
        if d.get("name") == name and d.get("password") == password:
             return {"name": name, "valid": True,
                     "message":f"Hello Dear {name}"
                     }
        
    else:
        return {"message": f"Sorry, {name} is not a valid user"}    

# The path function / web endpoint:
@app.get("/user")
def get_user(user: Annotated[dict, Depends(user_dep)]) -> dict:
    return user
