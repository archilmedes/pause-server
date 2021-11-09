from http.server import BaseHTTPRequestHandler, HTTPServer
from pynput.keyboard import Key, Controller
import urllib.parse

class GP(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def do_HEAD(self):
        self._set_headers()
    def do_GET(self):
        self._set_headers()
        if 'favicon' not in self.path:
            keyboard = Controller()
            keyboard.press(' ')
            keyboard.release(' ')

def run(server_class=HTTPServer, handler_class=GP):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Server running at localhost:8000...')
    httpd.serve_forever()

run()
