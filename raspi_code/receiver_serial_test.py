from time import sleep
import serial
from struct import pack
from time import sleep

print("Starting...")
ser = serial.Serial(port='/dev/ttyACM0', # ls /dev/tty* to find your port
		baudrate = 9600,
		parity = serial.PARITY_NONE,
		stopbits = serial.STOPBITS_ONE,
		bytesize = serial.EIGHTBITS,
		timeout = 1)
print("Initialized serial communication")

negative_byte = 0b1000000000000000
position_value_byte = 0b0100000000000000

while True:
    result = ser.read(ser.inWaiting())
    print(result)
    sleep(100)

