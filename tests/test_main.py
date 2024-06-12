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
    The test_index function tests the index route of our application.
    It does this by making a GET request to the / endpoint and checking that
    the response has a status code of 200 (OK) and that the content-type header is set to text/html; charset=utf-8.

    :return: A response with a 200 status code and the correct content type
    :doc-author: Trelent
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"


def test_predict_api():
    """
    The test_predict_api function tests the predict_api function in main.py.
    It does this by creating a new image, saving it to a file-like object, and then sending that file-like object as an argument to the /predict/image endpoint of our API.
    The test passes if we get back an HTTP 200 response code and if the content type is HTML.

    :return: A 200 status code and the content type is text/html; charset=utf-8
    :doc-author: Trelent
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
