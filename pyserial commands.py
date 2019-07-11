import serial
import time


def forw():
	ser= serial.Serial('COM11',9600)
	xc=ser.read()
	ser.write(b'f')
	time.sleep(0.2)
	ser.write(b's')
	time.sleep(0.2)
	print("forward")
	ser.close()
def righ():
	ser= serial.Serial('COM11',9600)
	xc=ser.read()
	ser.write(b'r')
	time.sleep(0.2)
	ser.write(b's')
	time.sleep(0.3)
	print("right")
	ser.close()
def ligh():

	ser= serial.Serial('COM11',9600)
	xc=ser.read()
	ser.write(b'l')
	time.sleep(0.2)
	ser.write(b's')
	time.sleep(0.3)
	print("left")
	ser.close()
def bac():
	ser= serial.Serial('COM11',9600)
	xc=ser.read()
	ser.write(b'b')
	time.sleep(0.2)
	ser.write(b's')
	time.sleep(0.3)
	print("back")
	ser.close()
def frigh():
	ser= serial.Serial('COM11',9600)
	xc=ser.read()
	ser.write(b'r')
	time.sleep(0.3)
	ser.write(b's')
	time.sleep(0.2)
	print("right")
	ser.close()
def fullright():
	t=11
	while(t):
		frigh()
		t-=1
