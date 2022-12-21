FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3.11 python3.11-distutils

RUN apt-get install -y python3-pip

RUN pip install pyTelegramBotAPI

RUN pip install aioschedule

RUN pip install aiohttp

COPY bot.py bots/bot.py

CMD ["python3", "bots/bot.py"]