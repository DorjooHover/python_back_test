FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory


# Create a virtual environment
RUN python -m venv venv

# Activate the virtual environment
SHELL ["cmd", "/S", "/C", "venv\\Scripts\\activate.bat"]

# Install the project dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the entire project directory to the working directory
COPY . .

# Set the command to run your Python application with Uvicorn
CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "$PORT"]