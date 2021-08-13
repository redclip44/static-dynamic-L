import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv.bind(('0.0.0.0', 8000))#172.31.201.138,u188123105
serv.listen(5)
while True:
	conn, addr = serv.accept()
	from_client = ''
	while True:
		data = conn.recv(4096)
		if not data:
			break
		from_client += data
		print from_client
	conn.close()
	print('client disconnected')
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(('172.31.251.155', 8000))
	client.send("I am CLIENT<br>")
	from_server = client.recv(4096)
	client.close()
	print(from_server)
