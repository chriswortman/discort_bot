FROM ubuntu:bionic

COPY bot.py /bot.py
COPY quotes.json /quotes.json

RUN apt-get update && apt-get install -y python3.8 python3-pip
RUN python3 -m pip install discord.py discordhealthcheck

HEALTHCHECK CMD discordhealthcheck || exit 1
CMD python3 bot.py

