FROM python:3.13.1-slim

WORKDIR /src

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /logs && chmod 777 /logs

CMD ["python", "-m", "src.bot.main"]