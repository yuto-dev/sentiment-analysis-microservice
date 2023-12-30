FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN apt-get update
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
