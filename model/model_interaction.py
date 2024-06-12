import keras
import numpy as np

from io import BytesIO
from PIL import Image


model = None

filepath = "model/models/vgg16_basesd_model_2_VGG16.hdf5"

class_names = [
    "Літак",
    "Автомобіль",
    "Птах",
    "Кіт",
    "Олень",
    "Пес",
    "Жаба",
    "Кінь",
    "Корабель",
    "Вантажівка",
]


def load_model():
    """
    The load_model function loads the model from a filepath.
    
    :return: A trained model
    :doc-author: Trelent
    """
    model = keras.models.load_model(filepath)

    return model


def predict(image: Image.Image):
    """
    The predict function takes an image as input and returns a string
        describing the object in the image.

    :param image: Image.Image: Pass the image to the function
    :return: A string with the class name
    :doc-author: Trelent
    """
    global model
    if model is None:
        try:
            model = load_model()
        except Exception as e:
            print("Неправильна модель, помилка", e)

    image = np.asarray(image.resize((32, 32)))[..., :3]
    image = np.expand_dims(image, 0)
    image = image / 255.0

    result = model.predict(image)
    response = class_names[np.array(result).argmax()]
    return f"Class: {response}"


def read_imagefile(file) -> Image.Image:
    """
    The read_imagefile function takes a file object and returns an Image.Image object.

    :param file: Read the image file
    :return: An image object
    :doc-author: Trelent
    """
    image = Image.open(BytesIO(file))

    return image
