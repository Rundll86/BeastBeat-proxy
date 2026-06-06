import json

from flask import Flask, request
import requests
import time

from engine.config import PROXY_PORT
from engine.constants import CURRENT_USER, JOKE
from engine.dir import use_base

app = Flask(__name__)


@app.route("/oauth2/authorize")
def root():
    time.sleep(0.1)
    requests.get(
        request.args["redirect_uri"],
        params={
            "code": JOKE,
            "state": "None",
        },
    )
    return "授权完成！！！"


@app.route("/api/oauth2/token", methods=["post"])
def token():
    return json.dumps(
        {
            "access_token": JOKE,
            "token_type": "Bearer",
            "expires_in": 3600,
            "refresh_token": JOKE,
            "scope": "read write",
        },
        ensure_ascii=False,
    )


@app.route("/api/oauth2/api/current_user")
def current_user():
    return json.dumps(CURRENT_USER, ensure_ascii=False)


def start():
    app.run(
        "0.0.0.0",
        port=PROXY_PORT,
        ssl_context=(
            use_base("cert.pem"),
            use_base("key.pem"),
        ),
    )
