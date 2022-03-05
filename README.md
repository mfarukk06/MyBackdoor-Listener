This project contains the following,
```
1-) Backdoor python script
2-) Backdoor Listener Framework
```

MySocket.py is the backdoor script that you can use it to create a bridge between target's and your machine. If you inject this file into a target machine and target machine run it, you can upload, download files to/from target machine.(Some Firewalls can delete MySocket.py because they see it dangerous. If you want it to be undetectable you can look for the subjects like "FUD" , "Hex Editing")

MySocketListener.py is the Backdoor Framework that you can see all of the target machine's files. Also you can download upload file to/from target machine.

USAGE: 
```
1-) Run MySocketListener.py from your device and wait for target machine to run MySocket.py(You can use to be more attractive to target by using your Social Engineering Skills)
2-) When target open MySocket.py, you can reach all of the target computer files from MySocketListener.py and upload or download files to it or from it
```

TERMINAL CODES TO WORK:
```
1-) cd root/PycharmProjects/MySocketListener(Your listener file location)
2-) python3 MySocketListener.py
3-) Wait for the target to run MySocket.py
4-) Done! You can download upload files to target machine and see all of the files in it. (Use Windows cmd codes to manage the Backdoor Listener)
```
