# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import time

from sanic import Sanic
from sanic.response import json
from multiprocessing import Manager

app = Sanic("myapp")



class Features:
    Name: str
    Age: int


fe = Features()
fe.Name = "cjw"
fe.Age = 1


myDict = Manager().dict()


@app.route("/")
async def test(request):
    myDict["fe"]["Age"] += 1
    return json({"hello": "pid:{} world {}".format(os.getpid(), myDict["fe"]["Age"])})


@app.route("/hello")
async def hello(request):
    myDict["fe"]["Age"] += 2
    return json({"hello": "pid:{} world {}".format(os.getpid(), myDict["fe"]["Age"])})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, workers=4)
