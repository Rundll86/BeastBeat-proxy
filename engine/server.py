import json

from flask import Flask, request
import requests
import time

from engine.constants import CURRENT_USER

app = Flask(__name__)


@app.route("/oauth2/authorize")
def root():
    time.sleep(0.1)
    requests.get(
        request.args["redirect_uri"],
        params={
            "code": "NiHaoBeastBeat",
            "state": "None",
        },
    )
    return "授权成功，返回BeastBeat窗口后稍等既可。"


@app.route("/api/oauth2/token", methods=["post"])
def token():
    return json.dumps(
        {
            "access_token": "NiHaoBeastBeat",
            "token_type": "Bearer",
            "expires_in": 3600,
            "refresh_token": "NiHaoBeastBeat",
            "scope": "read write",
        },
        ensure_ascii=False,
    )


@app.route("/api/oauth2/api/current_user")
def current_user():
    return json.dumps(CURRENT_USER, ensure_ascii=False)
