from fastapi.testclient import TestClient

from PIL import Image
from io import BytesIO

import main
import sys
import os

sys.path.append(os.getcwd())

client = TestClient(main.app)


def test_index():
    """
   The test_index work tests the list course of our application.
    It does this by making a GET request to the / endpoint and checking that
    the reaction features a status code of 200 (OK) which the content-type header is set to text/html; charset=utf-8.

    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"


def test_predict_api():
    """
    The test_predict_api work tests the predict_api work in main.py.
    It does this by making a modern picture, sparing it to a file-like protest, and after that sending that file-like protest as an contention to the /predict/image endpoint of our API.
    The test passes on the off chance that we get back an HTTP 200 response code and on the off chance that the substance sort is HTML. 

    """
    file_data = BytesIO()
    image = Image.new("RGB", size=(32, 32), color=(255, 0, 0))
    image.save(file_data, "jpeg")
    file_data.seek(0)

    response = client.post(
        "/predict/image", files={"file": ("test.jpg", file_data, "image/jpeg")}
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
