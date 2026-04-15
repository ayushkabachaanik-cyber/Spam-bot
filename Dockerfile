FROM python:3.13-slim

RUN apt-get update && apt-get install -y --no-install-recommends git curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app/
COPY . /app/
RUN python3 -m pip install --no-cache-dir -r requirements.txt
CMD ["python3", "main.py"]
