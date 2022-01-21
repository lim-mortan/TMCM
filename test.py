from serial import Serial    
import pyTMCL
from time import sleep

MODULE_ADDRESS = 0
serial_port = Serial("COM4")

bus = pyTMCL.connect(serial_port)

motor = bus.get_motor(MODULE_ADDRESS)
motor.rotate_left(1000)
sleep(2)
motor.stop()