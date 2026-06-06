import os
import sys
import __main__

from engine import hosts, certificate, server

print(
    os.path.abspath(sys.argv[0]),
    os.path.dirname(os.path.abspath(sys.argv[0])),
    __main__.__file__,
)
if False:
    hosts.setup()
    certificate.setup()
    server.start()
