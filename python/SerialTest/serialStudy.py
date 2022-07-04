import serial 

values = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
s = serial.Serial("COM4", 9600) 
s.write(b'Hello') 
s.write(bytearray(values)) 
while True: 
    data = s.readline() 
    print(data) 
s.close()

