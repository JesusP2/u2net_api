from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import io
import os
import uuid
from PIL import Image

from u2net_test import main


app = FastAPI()


@app.post('/remove_background')
async def remove_background(image: UploadFile = File(...)):
    #READ AND SAVE IMG
    img_bytes = await image.read()
    stream =io.BytesIO(img_bytes)
    img =Image.open(stream)
    uid =uuid.uuid4().hex
    img.save(f'./test_data/test_images/{uid}.png')
    img.save(f'./test_data/images/{uid}.png')
    main()
    os.remove(f"./test_data/test_images/{uid}.png")
    mask = Image.open(f"./test_data/u2net_results/{uid}.png").convert("L")
    img.putalpha(mask)
    img.save(f"./test_data/background_removed/{uid}.png")

    return FileResponse(f"./test_data/background_removed/{uid}.png")
