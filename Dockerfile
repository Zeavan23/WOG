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

# Set the USERNAME environment variable (adjust as needed)
ENV USERNAME="default_user"

# Run MainScore.py when the container launches
CMD ["python", "main_scores.py"]
