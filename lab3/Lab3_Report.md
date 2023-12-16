# Лабораторная работа №3
<img src="/pics/titul2.jpg" alt="Титульный лист">

### Цель работы: 
Сделать, чтобы после пуша в наш репозиторий автоматически собирался докер образ и результат его сборки сохранялся куда-нибудь.

### Ход работы

Мы сделали python файл mаin.py, который представляет из себя простейший Flask-сервер, работающий на порту 8121. По адресу / выводится удвоененное значение заданного в функцию аргумента. 

1) Написать скрипт (`main.py`), с которым в дальнейшем будет проведена работа.

```python
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def get_env_string():
    return f(34.5)

def f(x):
    return str(2*x)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8121)
```

2) Создать файл с тестами для `main.py` - `test.py`

```python
import unittest
from server import f

tc = unittest.TestCase('__init__')

tc.assertEqual(f(2), '4')
tc.assertEqual(f(3), '6')
tc.assertEqual(f(4), '8')
tc.assertEqual(f(5), '10')
```

3) Сгенерируем `requirements.txt` для успешкой сборки:

```python
pip3 freeze > requirements.txt
```

4) Пишем `Dockerfile`

``` Dockerfile
FROM python:3.12
COPY ./server.py /task2/
RUN pip install Flask
WORKDIR /task2/
ENTRYPOINT ["python", "server.py"]
EXPOSE 8121
```
5) В настройках репозитория добавить Actions Secrets: DOCKER_PASSWORD и DOCKER_USERNAME. Это нужно для того, чтобы в целях безопасности в дальнейшем не прописывать в скрипте логин и пароль от учетной записи приватного Docker-Registry.

6) Написать `workflow` `cicd.yml` в папке `.github/workflows`

После чего совершается проверка в разделе Actions, по итогу, все проверки завершены успешно:

<img src="/pics/3.1.jpg" alt="">


### Вывод:
В ходе выполнения данной лабораторной работы была осуществлена автоматическая сборка Docker образа с его автоматической выгрузкой на сервер, который нам предоставил наш `Добрый друг` (https://dmitriy.space/CV.pdf).
