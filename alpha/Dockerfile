FROM python:3.6
WORKDIR /fastapi
COPY requirements.txt /fastapi
RUN apt-get update
RUN pip install -r requirements.txt

# Define environment variable
COPY ./app /fastapi/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
