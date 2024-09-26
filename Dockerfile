# Use an official Python runtime as a parent image
FROM python:3.11.4-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for Django
EXPOSE 8000

# Run Django's migration and collectstatic command
RUN python manage.py collectstatic --noinput

# Run the application using Gunicorn
CMD ["gunicorn", "happy_grad_fin.wsgi:application", "--bind", "0.0.0.0:8000"]
