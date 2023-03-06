# Use the official Python image as base
FROM python:3.9-slim-buster

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENVIRONMENT production

# Set work directory
WORKDIR /code

# Copy project files to work directory
COPY . /code/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for web traffic
EXPOSE 8000

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]