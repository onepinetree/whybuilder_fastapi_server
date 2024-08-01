from fastapi import FastAPI
from urllib.parse import unquote
import uvicorn
from pydantic import BaseModel


app = FastAPI()

class Model(BaseModel):
    climax: int 
    time_back: int  
    url: str


@app.get("/items")
def modify_link(model: Model):

    base_link: str = model.url
    base_link = unquote(base_link)

    request_start_time : int = model.climax - model.time_back
    
    if 't=' in base_link:
        base_link = base_link.split('t=')[0]

    modified_link = f'{base_link}&t={request_start_time}s'

    return {"modified_url": modified_link}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
