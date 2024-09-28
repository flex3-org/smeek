# Use the official Python slim image
FROM ubuntu:latest

# Set the working directory
WORKDIR /app

# Install git, python3, and virtualenv
RUN apt-get update && apt-get install -y git python3 python3-pip python3-venv

# Create and activate a virtual environment
RUN python3 -m venv venv
ENV PATH="/app/venv/bin:$PATH"

# Copy the requirements file
COPY requirements.txt requirements.txt

# Install Python dependencies in the virtual environment
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the command to run the application
CMD ["uvicorn", "main:app", "--reload"]
