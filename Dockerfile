FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY talaba.proto *.py ./
# Kod generatsiyasi obraz qurilayotganda bajariladi
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. talaba.proto
ENV PYTHONUNBUFFERED=1
EXPOSE 50051
CMD ["python", "server.py"]
