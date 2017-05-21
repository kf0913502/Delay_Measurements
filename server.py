import socket
import threading
import time
import struct


terminated = False



def getTCPInfo(s):
	fmt = "B"*7+"I"*21
	x = struct.unpack(fmt, s.getsockopt(socket.IPPROTO_TCP, socket.TCP_INFO, 92))
	tcpInfo = {"state" : x[0],
		"ca_state" : x[1],
		"retransmits": x[2],
		"probes": x[3],
		"backoff": x[4],
		"options": x[5],
		"sndwscale+rcvwscale" : x[6],
		"rto" : x[7],
		"ato": x[8],
		"snd_mss": x[9],
		"rcv_mss": x[10],
		"unacked": x[11],
		"sacked" : x[12],
		"lost" : x[13],
		"retrans": x[14],
		"fackets": x[15],
		"last_data_sent": x[16],
		"last_ack_sent": x[17],
		"last_data_recv" : x[18],
		"last_ack_recv" : x[19],
		"pmtu": x[20],
		"rcv_ssthresh": x[21],
		"rtt": x[22],
		"rttvar": x[23],
		"snd_ssthresh" : x[24],
		"snd_cwnd" : x[25],
		"advmss": x[26],
		"reordering": x[27]}

	return tcpInfo


def readLine(sck):
	char = ""
	line = ""
	while(char != "\n"):
		line += char
		char = str(sck.recv(1))
		if (char == ""):
			return ""
	return line


def handleConnection(sck, addr,data):
	global terminated
	print data
	rate = float(data.split('\n')[0])
	rate = rate * 1024 * 1024
	packet = '0'*1470
	bytesSent = 0
	startTime = time.time()
	while not terminated:
		try:
			elapsedTime = time.time() - startTime
			if (elapsedTime * rate >= bytesSent * 8):
				sck.sendto(packet,addr)
				bytesSent += 1500
		except KeyboardInterrupt:
			terminated = True
			break
sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sck.bind(('10.6.42.191', 9000))


while not terminated:
	try:
		data, addr = sck.recvfrom(1470)

		p2 = threading.Thread(target=handleConnection, args=(sck,addr,data,))
		p2.start()
	except KeyboardInterrupt:
		terminated = True
		break
