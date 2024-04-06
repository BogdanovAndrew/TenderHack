from fastapi import FastAPI
import uvicorn

import service


app = FastAPI(title="Tender Hack")

app.include_router(service.router)

@app.get('/')
def index():
    return {'msg': 'OK'}


if __name__ == '__main__':
    uvicorn.run(app)