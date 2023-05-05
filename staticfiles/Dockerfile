FROM python:3.9

# Install system dependencies
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/*

# Create virtual environment and set it as default Python environment
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE $PORT
# Copy the rest of the application code
COPY . /app

# Set the working directory
WORKDIR /app

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:PORT"]
