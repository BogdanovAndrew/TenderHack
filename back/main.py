from fastapi import FastAPI
import uvicorn


app = FastAPI(title="Tender Hack")

@app.get('/')
def index():
    return {'msg': 'OK'}


if __name__ == '__main__':
    uvicorn.run(app)