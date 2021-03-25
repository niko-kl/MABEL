from approxeng.input.selectbinder import ControllerResource
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
while True:
    try:
        with ControllerResource() as joystick:
            print('Found a joystick and connected')
            while joystick.connected:
                sendByte = 0b00000000
                left_x = joystick['lx']
                left_y = joystick['ly']
                #print("(x/y) = (" + str(left_x) + "/" + str(left_y) + ")")
                if not(left_x == 0 and left_y == 0):
                    if left_x < 0:
                        print("Moving left")
                        sendByte |= 0b00000001
                    if left_x > 0:
                        print("Moving right")
                        sendByte |= 0b00000010
                    if left_y > 0:
                        print("Moving forward")
                        sendByte |= 0b00000100
                    if left_y < 0:
                        print("Moving backwards")
                        sendByte |= 0b00001000
                    val = pack("B", sendByte)
                    ser.write(val)
                sleep(0.05)
        # Joystick disconnected...
        print('Connection to joystick lost')
    except IOError:
        # No joystick found, wait for a bit before trying again
        print('Unable to find any joysticks')
        sleep(1.0)