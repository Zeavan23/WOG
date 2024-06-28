# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8777 available to the world outside this container
EXPOSE 8777

# Run main_score.py when the container launches
CMD ["python", "main_score.py"]
