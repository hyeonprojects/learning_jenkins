from fastapi import FastAPI

app = FastAPI(title='You want auto depoly')


@app.get('/')
async def auto_depoly():
    return 'you success depoly!!'
