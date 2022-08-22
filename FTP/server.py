from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


addr = ('127.0.0.1', 21)        # ftp://127.0.0.1
path = './storage'
authorizer = DummyAuthorizer()
authorizer.add_user('admin', 'password', path, perm='elradfmw')

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(addr, handler)
server.serve_forever()
