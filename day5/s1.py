# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server


def RunServer(environ, start_response):
    start_response(status = '200 OK', headers = [('Content-Type', 'text/html')])
    url = environ['PATH_INFO']
    return 'Whisky YM'

if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print 'Serving HTTP on port 8000...'
    httpd.serve_forever()

