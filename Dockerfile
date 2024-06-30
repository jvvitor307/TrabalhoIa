FROM python:3.10

WORKDIR /code

COPY . .

RUN pip install --no-cache-dir --upgrade -r requeriments.txt


CMD ["python", "main.py"]