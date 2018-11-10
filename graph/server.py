import socket
from node import *
from bsonrpc import JSONRpc
from bsonrpc import request, service_class
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)

def toTree(dict):
  children = list(dict)
  return children

# Class providing functions for the client to use:
@service_class
class ServerServices(object):

  @request
  def increment(self, root):
    return increment(root)

  @request
  def printFromServer(self, listDict):
    for l in listDict:
      print(l[0], ":", l[1])


# Quick-and-dirty TCP Server:
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('localhost', 50001))
ss.listen(10)

while True:
  s, _ = ss.accept()
  # JSONRpc object spawns internal thread to serve the connection.
  JSONRpc(s, ServerServices(),framing_cls=JSONFramingNone)
