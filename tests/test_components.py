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
    The record work makes a record protest that can be utilized to test the show.
        The work returns a record question with an picture of measure 100x100 and color ruddy.

    """
    file_data = BytesIO()
    image = Image.new("RGB", size=(100, 100), color=(255, 0, 0))
    image.save(file_data, "jpeg")
    file_data.seek(0)

    return file_data


def test_load_model():
    """
    The test_load_model work tests the load_model work in model/model_interaction.py
        The test checks that the result of calling load_model is an occurrence of demonstrate, which may be a lesson characterized in model/Model.py 

    """
    result = model_components.load_model()
    assert isinstance(result, Model)


def test_read_imagefile(file):
    """
    The test_read_imagefile work tests the read_imagefile work in model_interaction.py
        The test checks that the result of calling read_imagefile is an occurrence of JpegImagePlugin.JpegImageFile 

    """
    result = model_components.read_imagefile(file.read())
    assert isinstance(result, JpegImagePlugin.JpegImageFile)


def test_predict(file):
    """
    The test_predict work tests the foresee work in model_interaction.py
        The test_predict work takes a record as an contention and peruses it into memory.
            It at that point passes that picture to the foresee work, which returns a string of
            anticipated names for that image. The test attests that this returned esteem isundoubtedly a string. 
    
    """
    image = model_components.read_imagefile(file.read())
    result = model_components.predict(image)
    assert isinstance(result, str)
