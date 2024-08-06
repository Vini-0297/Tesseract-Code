# Use a Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY app.py app.py

# Expose the port the app runs on
EXPOSE 80

# Define the command to run the application
CMD ["python", "app.py"]
