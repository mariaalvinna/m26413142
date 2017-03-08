#/usr/bin/python
f = open("fruits.txt")
line = f.readline()
while line:
	print(line)
	line = f.readline()
f.close()
