FROM python:3.9-slim
# Adicione esta linha:
ENV PYTHONUNBUFFERED=1 
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]
