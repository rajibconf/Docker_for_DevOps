FROM python:3.12-slim

LABEL version="0.0.1"
LABEL description="Python Program Docker Image for DevOps"
LABEL maintainer="rajib.conf@gmail.com"

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "fastAPI-demo:app", "--host", "0.0.0.0", "--port", "8000"]
