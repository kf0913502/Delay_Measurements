import socket
import struct
import time
import sys

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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, 25, sys.argv[4]+'\0')

s.connect((sys.argv[1], int(sys.argv[2])))
s.send(sys.argv[3] + "\n")
startTime = time.time()
bytesReceived = 0
while(True):
	try:
		data = s.recv(30000)
		bytesReceived += len(data)
		print "rate: ", ((bytesReceived * 8) / (time.time() - startTime))/(1024*1024)
		print getTCPInfo(s)['rtt']
	except KeyboardInterrupt:
		break
