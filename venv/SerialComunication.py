#!/usr/bin/env python3
import serial
import time
import random

from rclpy.node import Node

from std_msgs.msg import String

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()

    while True:
        vs = random.randint(0,90)
        ser.write(str(vs).encode('utf-8'))
        time.sleep(30000)
