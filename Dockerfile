# FROM python:3.9-bullseye
# WORKDIR /app
# COPY requirements.txt  requirements.txt
# RUN pip3 install -r requirements.txt
# COPY . .
# CMD ["python3" ,"manage.py" ,"runserver","0.0.0.0:8000"]


FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
