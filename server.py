from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from Functions import (frames as fr)
# server
app = FastAPI()

@app.get("/")
async def root():
    index = fr.findCamIndex()
    if index == None:
        return {"Message": "Nenhuma câmera foi encontrada"}
    media_type = 'multipart/x-mixed-replace; boundary=frame'
    return StreamingResponse(fr.gen_frames(index), media_type=media_type) 