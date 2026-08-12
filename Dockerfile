FROM python:3.13.1-slim

WORKDIR /rybatgbot

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-m", "src.bot.main"]