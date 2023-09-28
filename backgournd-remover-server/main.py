from rembg import remove
from fastapi import FastAPI, File, UploadFile
import uuid
import os
from random import randint
# from fastapi.responses import FileResponse



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


# @app.get("/show/")
# async def read_random_file():
 
#     # get random file from the image directory
#     files = os.listdir(IMAGEDIR)
#     random_index = randint(0, len(files) - 1)
 
#     path = f"{IMAGEDIR}{files[random_index]}"
     
#     return path

# @app.get("/result/")
# async def remobe_bg():
#     files = os.listdir(IMAGEDIR)
#     random_index = randint(0, len(files) - 1)
 
#     path = f"{IMAGEDIR}{files[random_index]}"

#     with open(path, 'rb') as i:
#         output_path = f"{uuid.uuid4()}.jpg"
#         with open(f"{IMAGEDIR}{output_path}", 'wb') as o:
#             input = i.read()
#             output = remove(input)
#             o.write(output)
#     return output_path


