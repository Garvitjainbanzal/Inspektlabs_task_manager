# Use an official Python runtime as a parent image
FROM python:3.11-alpine

# Set the working directory
WORKDIR /task_manager

# Copy the current directory contents into the container
COPY . /task_manager

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8013 available to the world outside this container
EXPOSE 8013

# Run app.py when the container launches
CMD ["python3", "main.py", "--host=0.0.0.0"]
