
FROM python:3.12

COPY ./server.py /task2/
RUN pip install Flask
ENV MESSAGE="Значение не установлено(("
VOLUME /data/
WORKDIR /task2/
ENTRYPOINT ["python", "server.py"]
EXPOSE 80 
