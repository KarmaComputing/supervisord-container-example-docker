from celery import Celery
import time
from flask import Flask

app = Flask(__name__)  # Flask
worker = Celery('tasks', broker='redis://localhost:6379/0')  # Celery decorator


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/background-task')
def slow_task():
    add.delay(1, 1)
    return 'Slow task has been scheduled!'


@worker.task
def add(x, y):
    time.sleep(5)
    return x + y


print("hello")
add.delay(1, 1)
print("Joel")
