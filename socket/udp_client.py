from socket import *

class UDPClient:
    def __init__(self, _serverName: str, _serverPort: int) -> None:
        self.serverName = _serverName
        self.serverPort = _serverPort

    def connect(self) -> None:
        _clientSocket = socket(AF_INET, SOCK_DGRAM)
        _clientSocket.bind(('', 5432))

        _message = str(input('Input Lowercase sentence: '))
        _clientSocket.sendto(_message.encode(), (self.serverName, self.serverPort))

        (_modifiedMessage, _serverAddress) = _clientSocket.recvfrom(2048)
        print(_modifiedMessage.decode())

        print("Closing client socket")
        _clientSocket.close()

udpServer = UDPClient('localhost', 12000)
udpServer.connect()