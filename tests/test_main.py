from fastapi.testclient import TestClient

from PIL import Image
from io import BytesIO

import main
import sys
import os

sys.path.append(os.getcwd())

client = TestClient(main.app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"


def test_predict_api():
    file_data = BytesIO()
    image = Image.new("RGB", size=(32, 32), color=(255, 0, 0))
    image.save(file_data, "jpeg")
    file_data.seek(0)

    response = client.post(
        "/predict/image", files={"file": ("test.jpg", file_data, "image/jpeg")}
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
