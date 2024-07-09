from socket import *

class TCPServer:
    def __init__(self, _serverPort) -> None:
        self.serverPort = _serverPort
        
    def establish(self) -> None:
        _serverSocket = socket(AF_INET, SOCK_STREAM) # SOCK_DGRAM => datagram (UDP) / SOCK_STREAM => streaming (TCP)
        _serverSocket.bind(('', self.serverPort))
        _serverSocket.listen(1) # number of clients that TCP Server listens
        print("Ready to accept client")
        
        while True:
            (_connectionSocket, _addr) = _serverSocket.accept()

            _sentence = _connectionSocket.recv(1048).decode()
            print(_sentence, _addr)
            _connectionSocket.send(_sentence.upper().encode())
            print("Closing Conneciton Socket")
            _connectionSocket.close()

tcp_server = TCPServer(12001)
tcp_server.establish()
