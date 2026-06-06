import subprocess

from engine.dir import use_base


def install(fp: str):
    try:
        subprocess.run(
            ["certutil", "-user", "-addstore", "ROOT", fp],
            check=True,
            capture_output=True,
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def setup():
    install(use_base("cert.pem"))
