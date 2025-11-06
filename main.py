from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}
    
#pashka add this comment
#pashka2 add this comment
