from fastapi import FastAPI
import uvicorn

from back.service import router as ste_router


app = FastAPI(title="Tender Hack")

app.include_router(ste_router)

@app.get('/')
def index():
    return {'msg': 'OK'}


if __name__ == '__main__':
    uvicorn.run(app)