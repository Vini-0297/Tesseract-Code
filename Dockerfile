FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y tesseract-ocr libtesseract-dev python3-pip && \
    apt-get clean

# Copy application code to the container
COPY . /app

# Set the working directory
WORKDIR /app

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Expose the application port
EXPOSE 5000

# Run the application
CMD ["python3", "app.py"]
