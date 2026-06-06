import json

from flask import Flask, request
import requests
import time
from engine.config import PROXY_PORT
from engine.constants import CURRENT_USER, JOKE
from engine.dir import use_base

app = Flask("BeastBeat Verifier")


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
    return "登录成功，返回游戏窗口即可。"


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
    print("服务器已启动！启动游戏点击 [Verify On Patreon] 即可自动登录。")
    print("-" * 10 + "\n")
    app.run(
        "0.0.0.0",
        port=PROXY_PORT,
        ssl_context=(
            use_base("cert.pem"),
            use_base("key.pem"),
        ),
    )
