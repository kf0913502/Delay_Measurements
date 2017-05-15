import socket
import threading
import time



terminated = False


def readLine(sck):
	char = ""
	line = ""
	while(char != "\n"):
		line += char
		char = str(sck.recv(1))
		if (char == ""):
			return ""
	return line


def handleConnection(sck):
	global terminated
	rate = float(readLine(sck))
	rate = rate * 1024 * 1024
	packet = '0'*1440
	bytesSent = 0
	startTime = time.time()
	while not terminated:
		try:
			elapsedTime = time.time() - startTime
			if (elapsedTime * rate >= bytesSent * 8):
				sck.send(packet)
				bytesSent += 1500
		except KeyboardInterrupt:
			terminated = True
			break
sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sck.bind(('', 9000))
sck.listen(50)

while not terminated:
	try:
		conn, addr = sck.accept()

		p2 = threading.Thread(target=handleConnection, args=(conn,))
		p2.start()
	except KeyboardInterrupt:
		terminated = True
		break
