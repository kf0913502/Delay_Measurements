


import socket
import struct
from multiprocessing import Process, Value
import multiprocessing
import time
import Queue
from ctypes import *






#def start_thread(conn, terminate, forwardQueue):

#			print myData[0] - lastSeq
#			lastSeq = myData[0]


#			print str(myData[0]) + " " + str(myData[1]) + " " + str(addr)


			
#			while(True):
#				conn.sendto(struct.pack("II"+str(len(data)-8) + "s",myData[0],myData[1],myData[2]), addr)



#			forwardQueue.put(myData[2])

			
#			forwardSock.send(myData[2])



#			length = mylong[0]
#			seq = mylong[1]
#			data = recvAll(conn,mylong[0])

			
#			print "length", length, " seq", seq, " ", data , "\n"
#			forwardQueue.put(data)
#			print data
			

#			packedData = struct.pack("II"+str(len(data))+"s",length,seq,data)

#			packedData = struct.pack("II5000s",5000,seq,sendData)
			

			
#			while(True):
#				totalSent=0
#				while(totalSent < len(packedData)):
#				totalSent += conn.send(packedData[totalSent:])
#
			
#		except socket.error as e:
#			print e


TCP_IP = ''
TCP_PORT = 5002
BUFFER_SIZE = 1500
queues = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((TCP_IP, TCP_PORT))

s.listen(5)
terminated = False;
sendData = "0"*10000
while(not terminated):
	c,a = s.accept()
	print "received connection"
	while(not terminated):
		try:
			data = list(c.recv(BUFFER_SIZE))
			#print "received data:", data
			while(True):
				c.send(sendData)  # echo
		except KeyboardInterrupt:
			terminated = 1;
			break
			print "exiting"
		except Exception as e:
			print e
			break


