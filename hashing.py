import hashlib

while True:
	string = input("String > ")
	print("Hash:", hashlib.sha512(string.encode('utf-8')).hexdigest())
