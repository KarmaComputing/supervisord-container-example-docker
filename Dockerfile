FROM python:3

WORKDIR /app/src

COPY . .

COPY supervisord.conf /etc/supervisord.conf

RUN pip install supervisor==4.2.4

ENTRYPOINT ["./entrypoint.sh"]
