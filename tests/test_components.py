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
    """
    The file function creates a file object that can be used to test the model.
        The function returns a file object with an image of size 100x100 and color red.


    :return: A file-like object
    :doc-author: Trelent
    """
    file_data = BytesIO()
    image = Image.new("RGB", size=(100, 100), color=(255, 0, 0))
    image.save(file_data, "jpeg")
    file_data.seek(0)

    return file_data


def test_load_model():
    """
    The test_load_model function tests the load_model function in model/model_interaction.py
        The test checks that the result of calling load_model is an instance of Model, which is a class defined in model/Model.py

    :return: A model object
    :doc-author: Trelent
    """
    result = model_components.load_model()
    assert isinstance(result, Model)


def test_read_imagefile(file):
    """
    The test_read_imagefile function tests the read_imagefile function in model_interaction.py
        The test checks that the result of calling read_imagefile is an instance of JpegImagePlugin.JpegImageFile


    :param file: Read the image file
    :return: The image file
    :doc-author: Trelent
    """
    result = model_components.read_imagefile(file.read())
    assert isinstance(result, JpegImagePlugin.JpegImageFile)


def test_predict(file):
    """
    The test_predict function tests the predict function in model_interaction.py
        The test_predict function takes a file as an argument and reads it into memory.
        It then passes that image to the predict function, which returns a string of 
        predicted labels for that image. The test asserts that this returned value is 
        indeed a string.
    
    :param file: Read the image file
    :return: A string
    :doc-author: Trelent
    """
    image = model_components.read_imagefile(file.read())
    result = model_components.predict(image)
    assert isinstance(result, str)
