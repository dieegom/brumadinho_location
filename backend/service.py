import json
from configparser import ConfigParser
from http.server import BaseHTTPRequestHandler, HTTPServer

from utils import return_vector


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response_only(200)

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        json_data = self.rfile.read(int(self.headers['Content-Length']))

        geo_point = json.loads(json_data)
        lat, lng = geo_point.get('lat',None), geo_point.get('lng', None)
        position = return_vector(lat, lng)
        if position:
            response = {
                'lat': position[0],
                'lng': position[1],
            }
        else:
            response = {}

        self.wfile.write(json.dumps(response).encode())


def run(host='127.0.0.1', port=8000):
    server_address = (host, port)
    httpd = HTTPServer(server_address, Handler)
    # run_server
    httpd.serve_forever()


if __name__ == '__main__':
    cfg = ConfigParser()
    cfg.read('config.ini')
    cfg_port = cfg.getint('server', 'port')
    cfg_host = cfg.get('server', 'host')

    HOST_NAME = cfg_host
    PORT_NUMBER = cfg_port

    run(HOST_NAME, PORT_NUMBER)
