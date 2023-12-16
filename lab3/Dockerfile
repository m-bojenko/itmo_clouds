FROM python:3.12
COPY ./server.py /task2/
RUN pip install Flask
WORKDIR /task2/
ENTRYPOINT ["python", "server.py"]
EXPOSE 8121
