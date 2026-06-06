from engine.config import PROXY_PORT
from engine.hosts import setup_hosts
from engine.server import app

setup_hosts()
app.run(
    "0.0.0.0",
    port=PROXY_PORT,
    ssl_context=(
        "www.patreon.com+1.pem",
        "www.patreon.com+1-key.pem",
    ),
)
