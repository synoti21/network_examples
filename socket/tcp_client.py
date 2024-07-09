from socket import *

class TCPClient:
    def __init__(self, _serverPort: int, _serverName: str) -> None:
        self.serverPort = _serverPort
        self.serverName = _serverName

    def connect(self) -> None:
        _clientSocket = socket(AF_INET, SOCK_STREAM)
        _clientSocket.bind(('', 0))
        _clientSocket.connect((self.serverName, self.serverPort))

        _sentence = str(input('Input lowercase Sentence: '))
        _clientSocket.send(_sentence.encode())

        _modifiedSentence = _clientSocket.recv(1024)
        print("From server: ", _modifiedSentence.decode())
        _clientSocket.close()

tcp_client = TCPClient(12001, 'localhost')
tcp_client.connect()