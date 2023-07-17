# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Create a virtual environment
RUN python -m venv venv

# Activate the virtual environment
SHELL ["cmd", "/S", "/C", "venv\\Scripts\\activate.bat"]

# Install the project dependencies
RUN pip install uvicorn fastapi pymongo -r requirements.txt

# Copy the entire project directory to the working directory
COPY . .

# Set the command to run your Python application with Uvicorn
CMD ["uvicorn", "your_app_file:app", "--host", "0.0.0.0", "--port", "$PORT"]
