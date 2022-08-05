from fastapi import FastAPI,File, UploadFile


app=FastAPI()

@app.post("/files/")
async def create_files(file:bytes=File()):
    return {"filesize":len(file)}


@app.post("/uploadfile/")
async def create_files(file:UploadFile):
    return {"filename":file.filename}


