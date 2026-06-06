from engine.config import BASE_URL


HOSTS_ENTRY = "\n".join(
    [
        "# beastbeat-start",
        f"127.0.0.1 {BASE_URL}",
        "# beastbeat-end",
    ]
)
HOSTS_PATH = "C:/Windows/System32/drivers/etc/hosts"


def setup_hosts():
    cleanup_hosts()
    with open(HOSTS_PATH, "a", encoding="utf8") as f:
        f.write(HOSTS_ENTRY)


def cleanup_hosts():
    with open(HOSTS_PATH, "r", encoding="utf8") as f:
        content = f.read()
    with open(HOSTS_PATH, "w", encoding="utf8") as f:
        f.write(content.replace(HOSTS_ENTRY, ""))
