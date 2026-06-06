from flask import Flask, request
import requests
import time

app = Flask(__name__)


@app.route("/oauth2/authorize")
def root(path):
    time.sleep(3)
    requests.get(
        request.args["redirect_uri"],
        params={
            "code": "NiHaoBeastBeat",
            "state": "None",
        },
    )
    return "授权成功，返回BeastBeat窗口后稍等既可。"
