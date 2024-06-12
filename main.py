import os

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import subprocess
import traceback
from fastapi import FastAPI, File, UploadFile, HTTPException
from model.model_interaction import predict, read_imagefile
import uvicorn
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from html_response import response
from starlette.responses import HTMLResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def index():
    """
    The index function is the root of the API.
    It returns a FileResponse object, which is a file that can be read by any browser.
    
    
    :return: The index
    :doc-author: Trelent
    """
    return FileResponse("static/index.html")


@app.post("/run-jupyter/")
def run_jupyter():
    """
    The run_jupyter function starts a Jupyter Notebook server.

    :return: A dictionary with the message key and value
    :doc-author: Trelent
    """
    try:
        subprocess.Popen(["jupyter", "notebook"])
        return {"message": "Jupyter Notebook started successfully"}
    except Exception as e:
        return {"error": str(e)}


@app.post("/predict/image", status_code=200)
async def predict_api(file: UploadFile = File(...)):
    """
    The predict_api function is a FastAPI endpoint that accepts an uploaded image file,
        processes it with the predict function, and returns the prediction as a string.
    
    :param file: UploadFile: Pass the uploaded file to the function
    :return: A htmlresponse object with the prediction result
    :doc-author: Trelent
    """
    try:
        for f in os.scandir("static/upload"):
            os.remove(f.path)

        extension = file.filename.split(".")[-1] in ("jpg", "jpeg")
        if not extension:
            return HTMLResponse(
                content="<p id='upload-message' class='error'>Неправильний формат файлу</p>",
                status_code=400,
            )

        upload_dir = "static/upload/"
        os.makedirs(upload_dir, exist_ok=True)
        print(f"Директорія {upload_dir} створена або вже існує.")

        file_read = await file.read()
        if not file_read:
            print("Файл не прочитаний.")
            return HTMLResponse(
                content="<p id='upload-message' class='error'>Помилка при читанні файлу</p>",
                status_code=400,
            )
        print("Файл успішно прочитаний.")

        try:
            image = read_imagefile(file_read)
            print("Зображення успішно прочитане.")
        except Exception as e:
            print(f"Помилка при читанні зображення: {e}")
            traceback.print_exc()
            return HTMLResponse(
                content="<p id='upload-message' class='error'>Помилка при обробці зображення</p>",
                status_code=500,
            )

        try:
            prediction = predict(image)
            print("Прогноз успішно виконано.")
        except Exception as e:
            print(f"Помилка при прогнозуванні: {e}")
            traceback.print_exc()
            return HTMLResponse(
                content="<p id='upload-message' class='error'>Помилка при прогнозуванні</p>",
                status_code=500,
            )

        file_path = os.path.join(upload_dir, file.filename)
        print(f"Шлях до файлу: {file_path}")

        try:
            with open(file_path, "wb") as f:
                f.write(file_read)
            print("Файл успішно записаний.")
        except Exception as e:
            print(f"Помилка при записі файлу: {e}")
            traceback.print_exc()
            return HTMLResponse(
                content="<p id='upload-message' class='error'>Помилка при збереженні файлу</p>",
                status_code=500,
            )

        pred = response(f"{file.filename}", prediction)

        return HTMLResponse(content=pred, status_code=200)

    except Exception as e:
        print(f"Виникла помилка: {e}")
        traceback.print_exc()
        return HTMLResponse(
            content=f"<p id='upload-message' class='error'>Виникла внутрішня помилка сервера: {str(e)}</p>",
            status_code=500,
        )


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
