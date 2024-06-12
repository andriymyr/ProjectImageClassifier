# Згорткова нейронна мережа для класифікації зображень (CIFAR-10)

<p align="center">
   <img src="https://img.shields.io/badge/Language-Python-9cf">
   <img src="https://img.shields.io/badge/FastAPI-brightgreen">
   <img src="https://img.shields.io/badge/TensorFlow-2.15-orange">
   <img src="https://img.shields.io/badge/Pytest-informational">
   <img src="https://img.shields.io/badge/License-MIT-yellow">
</p>

## Опис

Даний проєкт представляє собою веб-застосунок із використанням згорткової нейронної мережі для класифікації зображень, який створений на навчальній базі датасету CIFAR-10.
Мета проєкту - навчання моделі та її подальше використання для розпізнавання 10 класів зображень: літаки, автомобілі, птахи, коти, олені, собаки, жаби, коні, кораблі та вантажівки.

## Встановлення та запуск

1. Клонуйте репозиторій:

```
git clone https://github.com/ValeraRishniak/Pythonistas_team_project.git
```

2. Перейдіть до директорії проєкту:

```
cd Pythonistas_team_project
```

pip install -r requirements.txt 3. Встановіть необхідні залежності:

```

```

4. Запустіть веб-інтерфейс:

```
python main.py
```

Також для користуванням застосунком ви можете використати створений образ з DockerHub

```
docker pull yamihelson/tpds
```

Для запуску застосунку :

```
docker run -p 8080:8080 yamihelson/tpds
```

Поряд із зазначеними варіантами запуску, нашою командою проведено деплой застосунку.
https://pythonistas-team-project.fly.dev/

## Використання

У разі запуску застосунку із Вашого локального ПК, відкрийте браузер та перейдіть за посиланням:

```
http://localhost:8000
```

У разі запуску через образ із DockerHub відкрийте браузер та перейдіть за посиланням:

```
http://localhost:8080
```

Натиснувши на кнопку **"Обрати файл"** Ви зможете обрати файл-зображення на Вашому ПК із розширенням .jpg та .jpeg. У випадку обранням файлу із іншим розширенням, програма поверне Вам повідомлення про неможливість його розпізнавання.

Після завантаження зображення, натисніть кнопку **"Класифікувати"** для визначення приналежності зображення до визначених класів.

Результат класифікації буде показаний під зображенням.

## Архітектура використаної нейронної мережі

Згорткова нейронна мережа має наступну архітектуру:
'''
Описание модели нейронной сети:
Входная форма: Модель предназначена для обработки изображений размером 32x32 пикселей и 3 цветовых каналов (RGB).

Слои:

Сверточные слои:

Модель начинается со слоя Conv2D с 32 фильтрами размером 3x3 и активацией ReLU. Пакетная нормализация применяется после каждой операции свертки.
Далее следуют еще два набора слоев Conv2D, каждый набор состоит из двух сверточных слоев с увеличивающимся количеством фильтров (2*num_filters и 4*num_filters) и активацией ac = 'relu'.
Пакетная нормализация применяется после каждой операции свертки.

Слои MaxPooling с размером пула 2x2 используются после каждого набора сверточных слоев для уменьшения пространственных размеров.

Выпадающие Dropout слои:
Слои исключения включаются после каждого набора сверточных слоев с частотой исключения 0, чтобы предотвратить переобучение.

Плотные слои:
Модель включает в себя четыре слоя Dense с 2048, 1024 и 512 единицами, за каждым из которых следует активация 'relu', пакетная нормализация и отсев (drop_dense=0.5) со скоростью 0,5.
Последний слой Dense имеет единицы измерения, равные количеству классов в наборе данных (обозначаемые num_classes), с функцией активации 'softmax' для многоклассовой классификации.

Регуляризация:
Для регуляризации ядра установлено значение (reg=None) для всех слоев.
Для плотных слоев не применяется определенная регуляризация ядра (reg2=None).
Функция активации: Функция активации 'relu' используется во всей модели.

Модельная компиляция:
Модель компилируется с использованием оптимизатора (from keras.optimizers import Adam()) с заданной скоростью обучения и другими параметрами.
Название модели: Модель называется «cifar10» и реализована с использованием последовательного API.

Эта архитектура модели подходит для задач классификации изображений, особенно в наборе данных CIFAR-10,
с постепенным уменьшением пространственных размеров за счет слоев свертки и объединения с последующими плотными слоями для классификации.
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

**Рішняк Валерій - Team lead**  
GitHub: https://github.com/ValeraRishniak

LinkedIn: https://www.linkedin.com/in/rishniakvaleriy/

**П'ятковська Вікторія - scrum master**  
GitHub: https://github.com/Vikka777

LinkedIn: https://www.linkedin.com/in/viktoriia-p-152100211/

**Маличок Денис - developer**  
GitHub: https://github.com/malychokd

LinkedIn: https://www.linkedin.com/in/denys-malychok-243520292/

**Мещеряков Антон - developer**

GitHub: https://github.com/Topsya

LinkedIn:

**Шевченко Сергій - developer**  
GitHub: https://github.com/Sergey-8057

LinkedIn: https://www.linkedin.com/in/shevchenko-sergiy/

## Ліцензія

Цей проєкт має ліцензію MIT.
