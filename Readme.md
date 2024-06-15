# Згорткова нейронна мережа для розпізнавання зображень (CIFAR-10)

<p align="center">
   <img src="https://img.shields.io/badge/Language-Python-9cf">
   <img src="https://img.shields.io/badge/FastAPI-brightgreen">
   <img src="https://img.shields.io/badge/TensorFlow-2.15-orange">
   <img src="https://img.shields.io/badge/Pytest-informational">
   <img src="https://img.shields.io/badge/License-MIT-yellow">
</p>

## Опис

Цей проект є веб-додатком, який використовує згорточні нейронні мережі для класифікації зображень і побудований на базі навчання датасету CIFAR-10.
Мета проекту — навчити модель і використовувати її  для розпізнавання 10 класів зображень:літаки, автомобілі, птахи, коти, олені, собаки, жаби, коні, кораблі та вантажівки.

## Встановлення та запуск

1. Клонуйте репозиторій:

```
git clone https://github.com/andriymyr/ProjectImageClassifier.git
```

2. Перейдіть до директорії проєкту:

```
cd ProjectImageClassifier
```

pip install -r requirements.txt 3. Встановіть необхідні залежності:

```
fastapi
matplotlib
matplotlib-inline
notebook
numpy
pandas
pandas-datareader
passlib
Pillow
pipenv
poetry
poetry-core
poetry-plugin-export
pydot
pytest
scikit-learn
scikit-surprise
scipy
seaborn
tensorboard
tensorboard-data-server
tensorflow
tensorflow-estimator
python-multipart
tensorflow-intel
tensorflow-io-gcs-filesystem
tomlkit
urllib3
uvicorn
virtualenv
virtualenv-clone
websocket-client
websockets
keras
lfs
jupyter
requests
docker

```

4. Запустіть веб-інтерфейс:

```
python main.py
```

## Використання

У разі запуску застосунку із Вашого локального ПК, відкрийте браузер та перейдіть за посиланням:

```
http://localhost:8000
```

Натисніть кнопку **Обрати файл**, щоб вибрати файли зображень із розширеннями .jpg і .jpeg на вашому ПК.
Якщо вибрати файл з іншим розширенням, програма поверне повідомлення про те, що файл не розпізнано.

Після завантаження зображення, натисніть кнопку **"Класифікувати"** для визначення приналежності зображення до визначених класів.

Результат класифікації буде показаний під зображенням.

## Архітектура використаної нейронної мережі

Згорткова нейронна мережа має наступну архітектуру:
'''
Опис моделі нейронної мережі:
Вхідна форма: Модель призначена для опрацювання зображень розміром 32x32 пікселів і 3 колірних каналів (RGB).

Шари розробки:

Згорткові шари:

Модель починається з шару Conv2D з 32 фільтрами розміром 3x3 і активацією ReLU. Пакетна нормалізація застосовується після кожної операції згортання.
Далі йдуть ще два набори шарів Conv2D, кожен набір складається з двох згортувальних шарів зі зростаючою кількістю фільтрів (2*num_filters і 4*num_filters) і активацією ac = 'relu'.
Пакетна нормалізація застосовується після кожної операції згортання.

Шари MaxPooling з розміром пулу 2x2 використовуються після кожного набору згорткових шарів для зменшення просторових розмірів.

Dropout шари, що випадають:
Шари виключення вмикаються після кожного набору згорткових шарів із частотою виключення 0, щоб запобігти перенавчанню.

Щільні шари:
Модель містить чотири шари Dense з 2048, 1024 і 512 одиницями, за кожним із яких слідує активація 'relu', пакетна нормалізація і відсів (drop_dense=0.5) зі швидкістю 0,5.
Останній шар Dense має одиниці виміру, що дорівнюють кількості класів у наборі даних (позначаються num_classes), з функцією активації 'softmax' для багатокласової класифікації.

Регуляризація:
Для регуляризації ядра встановлено значення (reg=None) для всіх шарів.
Для щільних шарів не застосовується певна регуляризація ядра (reg2=None).
Функція активації: Функція активації 'relu' використовується у всій моделі.

Модельна компіляція:
Модель компілюється з використанням оптимізатора (from keras.optimizers import Adam()) із заданою швидкістю навчання та іншими параметрами.
Назва моделі: Модель називається "cifar10" і реалізована з використанням послідовного API.

Ця архітектура моделі підходить для задач класифікації зображень, особливо в наборі даних CIFAR-10,
з поступовим зменшенням просторових розмірів завдяки шарам згортання та об'єднання з подальшими щільними шарами для класифікації.
'''

Model: "cifar10"

![Image](https://github.com/ValeraRishniak/Pythonistas_team_project/blob/main/model/model_info/model_info.jpg)

![Image](https://github.com/ValeraRishniak/Pythonistas_team_project/blob/main/model/model_info/model_visualition.png)

## Результати оцінки моделі.

Графіки показують точність та втрати моделі на тренувальних, тестових та валідаційних даних протягом навчання.

Графік точності  
![Image](https://github.com/ValeraRishniak/Pythonistas_team_project/blob/main/model/model_info/model_training_and_validation_accuracies.png)

Графік втрат  
![Image](https://github.com/ValeraRishniak/Pythonistas_team_project/blob/main/model/model_info/model_training_and_validation_losses.png)

Результати роботи моделі на тестових даних
![Image](https://github.com/ValeraRishniak/Pythonistas_team_project/blob/main/model/model_info/model_train_and_test_accuracy.png)

## Покриття тестами.

Роботу застосунку було протестовано на працездатність як тестами так і безпосередньо розробниками в якості звичайних користувачів.

![Image](https://github.com/ValeraRishniak/Pythonistas_team_project/blob/main/tests/tests_coverage.png)

## Автори

**Андрій Мирошниченко - Team lead**  

**Віктор Кос - scrum master** 

**Анатолій Перфілов - developer**

**Туркот Богдан - developer**

**Андрій Бузін - developer** 

## Ліцензія

Цей проєкт має ліцензію MIT.
