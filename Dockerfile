FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
COPY . .

# Set the command to run your Python application with Uvicorn
CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "$PORT"]