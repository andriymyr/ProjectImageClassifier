import pytest

# import keras
import model.model_interaction as model_components
import sys
import os


from PIL import Image, JpegImagePlugin
from io import BytesIO
from keras.models import Model

sys.path.append(os.getcwd())


@pytest.fixture()
def file():
    file_data = BytesIO()
    image = Image.new("RGB", size=(100, 100), color=(255, 0, 0))
    image.save(file_data, "jpeg")
    file_data.seek(0)

    return file_data


def test_load_model():
    result = model_components.load_model()
    # assert isinstance(result, keras.engine.sequential.Sequential)
    assert isinstance(result, Model)


def test_read_imagefile(file):
    result = model_components.read_imagefile(file.read())
    assert isinstance(result, JpegImagePlugin.JpegImageFile)


def test_predict(file):
    image = model_components.read_imagefile(file.read())
    result = model_components.predict(image)
    assert isinstance(result, str)
