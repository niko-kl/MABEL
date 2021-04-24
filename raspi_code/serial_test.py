from time import sleep
import serial
from struct import pack
from time import sleep

print("Starting...")
ser = serial.Serial(port='/dev/ttyACM1', # ls /dev/tty* to find your port
		baudrate = 9600,
		parity = serial.PARITY_NONE,
		stopbits = serial.STOPBITS_ONE,
		bytesize = serial.EIGHTBITS,
		timeout = 1)
print("Initialized serial communication")

negative_byte = 0b1000000000000000
position_value_byte = 0b0100000000000000

while True:
    negative = False
    input_number = int(input("input number: "))
    if input_number < 0:
        negative = True
        input_number *= -1
        input_number |= negative_byte
    input_number |= position_value_byte
    # print("modified number: ", input_number)

    first = input_number >> 8
    second = input_number & 255

    print("first number encoded: ", first)
    print("second number encoded: ", second)

    val = pack("B", first)
    ser.write(val)
    sleep(0.05)
    val = pack("B", second)
    ser.write(val)

