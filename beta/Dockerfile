# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install NLTK data (vader_lexicon)
RUN python -m nltk.downloader vader_lexicon

# Expose the port that FastAPI will run on
EXPOSE 8000

# Run FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
