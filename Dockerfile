# Dockerfile
FROM python:3.9

WORKDIR /app

# Install GDAL
RUN apt-get update && apt-get install -y libgdal-dev

# Upgrade pip
RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8506

COPY . .

CMD ["streamlit", "run", "main.py", "--server.port=8506", "--server.address=0.0.0.0"]
