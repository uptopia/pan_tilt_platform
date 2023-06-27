import serial 
import time
ser = serial.Serial("/dev/ttyUSB0", 9600)


s = "pp\n"
ser.write(s.encode())
time.sleep(0.1)

s = "pp100\n"
ser.write(s.encode())
time.sleep(0.1)

s = "pp0\n"
ser.write(s.encode())
time.sleep(0.1)

print(ser.readline().decode())
print(ser.readline().decode())
print(ser.readline().decode())
print(ser.readline().decode())