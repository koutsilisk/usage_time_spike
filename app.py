from flask import Flask, jsonify
from celery import Celery
from kmeans_usage import run
from time import process_time_ns
from celery.signals import task_prerun, task_postrun


d = {}

app = Flask(__name__)
celery = Celery(app.name, backend="redis://redis:6379/0", broker="redis://redis:6379/0")


@celery.task
def run_kmeans():
    res = run()


@task_prerun.connect
def task_prerun_handler(signal, sender, task_id, task, args, kwargs, **extras):
    d[task_id] = process_time_ns()


@task_postrun.connect
def task_postrun_handler(
    signal, sender, task_id, task, args, kwargs, retval, state, **extras
):
    try:
        cost = process_time_ns() - d.pop(task_id)
    except KeyError:
        cost = -1
    print(f"{task.__name__} took {cost} nanoseconds")


@app.route("/", methods=["GET"])
def index():
    return jsonify(message="Hello timetravelers")


@app.route("/kmeans", methods=["GET"])
def kmeans():
    run_kmeans.delay()
    return jsonify(message="started")
