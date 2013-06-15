import socket
from socket import *

def read_line(s):
	ret = ""
	while True:
		c = s.recv(1)
		if c == "\r\n" or c == "\n" or c == "":
			break
		else:
			ret += c
	ret += "\n"
	return ret

def conn(host, port):
	s = socket(AF_INET, SOCK_STREAM)
	s.connect((host, port))
	results = read_line(s)
	print results
	return s

def intro(s):
	results = read_line(s)
	results += read_line(s)
	results += read_line(s)
	return results

def go(direction, s):
	direction = direction + "\n"
	s.send(direction)
	results = read_line(s)
	results += read_line(s)
	results += read_line(s)
	return results

def navigate_maze(s):
	results = read_line(s)
	results += go("n", s)
	results += go("n", s)
	results += go("n", s)
	results += go("n", s)
	results += go("n", s)
	results += go("n", s)
	results += go("e", s)
	results += go("n", s)
	results += go("w", s)
	results += go("n", s)
	results += read_line(s)
	results += read_line(s)
	results += read_line(s)
#	results += read_line(s)
	return results

host = "diehard.shallweplayaga.me"
port = 4001

s = conn(host, port)

print intro(s)
print navigate_maze(s)

