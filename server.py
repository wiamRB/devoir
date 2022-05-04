
from xmlrpc.server import SimpleXMLRPCServer
def enr(objet):
    f = open('file.txt', 'r+')
    f.write(object) 
    return("ok")

server=Simple XMLRPCServer(("0.0.0.0",6789))
server.register_function(enr,"enr")
server.serve_forever()
