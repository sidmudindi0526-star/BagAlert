"""Simple HTTPS server for serving the Flutter PWA build locally.

Usage:  python serve_https.py
Then open https://10.0.0.150:4443 on your phone.
"""

import http.server
import ssl
import os

PORT = 4443
WEB_DIR = os.path.join(os.path.dirname(__file__), 'build', 'web')
CERT = os.path.join(os.path.dirname(__file__), '.cert', 'cert.pem')
KEY = os.path.join(os.path.dirname(__file__), '.cert', 'key.pem')

os.chdir(WEB_DIR)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(CERT, KEY)

server = http.server.HTTPServer(('0.0.0.0', PORT), http.server.SimpleHTTPRequestHandler)
server.socket = context.wrap_socket(server.socket, server_side=True)

print(f'Serving BagAlert PWA over HTTPS')
print(f'  Local:   https://localhost:{PORT}')
print(f'  Network: https://10.0.0.150:{PORT}')
print(f'  (Accept the self-signed certificate warning on your phone)')
server.serve_forever()
