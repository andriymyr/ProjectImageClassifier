# Вказуємо базовий образ Python
FROM python:3.11.0

# Встановимо залежності всередині контейнера
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Скопіюємо інші файли в робочу директорію контейнера
COPY . .

# Створюємо конфігураційний файл для Jupyter
RUN mkdir -p /root/.jupyter/
RUN echo "c.NotebookApp.password = u'$(python3 -c 'from notebook.auth import passwd; print(passwd("Dfea468opi$"))')'" > /root/.jupyter/jupyter_notebook_config.py

# Відкриваємо порти для FastAPI та Jupyter Notebook
EXPOSE 8080 8889

# Запустимо наш застосунок FastAPI всередині контейнера
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]



#docker build -t project_image_classifier . 