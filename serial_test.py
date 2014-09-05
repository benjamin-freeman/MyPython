import serial

t = serial.Serial('COM6',9600)
#t.open()
print(t.isOpen())
#s = "you are my world"
#n = t.write(s.encode())
print (t.portstr)
#print (n)

#while(t.available()>0):
#str = t.read(t.inWaiting())
line = t.readline()
while line:
	print(line.strip().decode("utf-8"))
	line = t.readline()
t.close()
#print (str.)