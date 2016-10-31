from __future__ import print_function
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import urlparse, parse_qs
import SocketServer
import urllib2
import json
import os
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

all_grades = {
    1: [10, 7.5, 8, 9.2],
    2: [3, 10, 9, 4],
    3: [5, 9, 6, 10]
}

user_service_base_url = os.environ.get('USER_SERVICE_BASE_URL', 'http://localhost:3000')

class S(BaseHTTPRequestHandler):
    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)

        try:
            user_data = urllib2.urlopen('%s/login/%s/%s' % (user_service_base_url, query_components['id'][0], query_components['password'][0])).read()
            user_data = json.loads(user_data)

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            id = int(query_components['id'][0])
            grades = all_grades[id]


            output = 'Grades for %s %s are: %s' % (user_data['name']['first'], user_data['name']['last'], grades)

            self.wfile.write(output)
        except Exception as e:
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            eprint(e)
            self.wfile.write('Something wrong happened')


def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port %s...' % port)
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
