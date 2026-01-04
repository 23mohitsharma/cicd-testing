FROM python.3.11-slim

WORKDIR /app

# 🔥 REQUIRED for LightGBM
RUN apt-get update && apt-get install -y \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*


COPY requirement.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8500
EXPOSE 8000

COPY . .

CMD ["bash" ,"-c","uvicorn app:app  --host 0.0.0.0 --port 8000 & streamlit run stream.py --server.port=8501 --server.address = 0.0.0.0"]