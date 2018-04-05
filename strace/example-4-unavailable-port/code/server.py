import SimpleHTTPServer
import SocketServer
import sys

PORT = 8000

try:
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print "serving at port", PORT
    httpd.serve_forever()
except:
    pass