# Use the official Python base image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y build-essential pkg-config libhdf5-dev && \
    apt-get install -y build-essential libgl1-mesa-glx libglib2.0-0

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Copy the test image file into the container
COPY img_to_text.jpeg /app

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python file into the container
COPY main.py .

# Run the Python file when the container launches
CMD ["python", "main.py"]
