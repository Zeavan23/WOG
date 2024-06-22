# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory to the working directory inside the container
COPY . .

# Install the dependencies from requirements.txt file
RUN pip install -r requirements.txt

# Expose the port on which the Flask app will run
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
