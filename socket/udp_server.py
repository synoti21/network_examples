from socket import *

class UDPServer:
    def __init__(self, _serverPort: int) -> None:
        self.serverPort = _serverPort

    def establish(self) -> None:
        _serverSocket = socket(AF_INET, SOCK_DGRAM)
        _serverSocket.bind(('', self.serverPort))
        print("The server is ready to receive")

        while True:
            (_message, _clientAddress) = _serverSocket.recvfrom(2048)
            _decodedMessage = _message.decode()
            print(_decodedMessage, _clientAddress)

            _serverSocket.sendto(_decodedMessage.upper().encode(), _clientAddress)

udpServer = UDPServer(12000)
udpServer.establish()