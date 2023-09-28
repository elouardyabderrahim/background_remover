from rembg import remove
from fastapi import FastAPI, File, UploadFile
import uuid



app = FastAPI()

IMAGEDIR = "images/"


@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
 
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)

    with open(f"{IMAGEDIR}{file.filename}", 'rb') as i:
        output_path = f"{uuid.uuid4()}.jpg"
        with open(f"{IMAGEDIR}{output_path}", 'wb') as o:
            input = i.read()
            output = remove(input)
            o.write(output)
    return output_path


