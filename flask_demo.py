#!/usr/bin/env python
# encoding: utf-8

import flask

import tornado.wsgi
import tornado.httpserver

app = flask.Flask(__name__)

@app.route('/')
def index():
  return "go to hell"

if __name__ == '__main__':
  port=5000
  http_server = tornado.httpserver.HTTPServer(tornado.wsgi.WSGIContainer(app))
  http_server.listen(port)
  print("Tornado server starting on port {}".format(port))
  tornado.ioloop.IOLoop.instance().start()
