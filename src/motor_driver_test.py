"""! @file motor_driver_test.py
This program tests the MotorDriver class by running a DC motor at various speeds.
"""

import pyb
import micropython
from motor_driver import MotorDriver

import utime

if __name__ == "__main__":
    
    try:
        
        # Setup motor driver using MotorDriver class.
        motor1 = MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, pyb.Timer(3, freq=20000))
        
        # Cycle motor through multiple duty cycles.
        while True:
            motor1.set_duty_cycle(30)
            utime.sleep(1)
            motor1.set_duty_cycle(60)
            utime.sleep(1)
            motor1.set_duty_cycle(100)
            utime.sleep(1)
            motor1.set_duty_cycle(120)
            utime.sleep(1)
            motor1.set_duty_cycle(0)
            utime.sleep(1)
            motor1.set_duty_cycle(-30)
            utime.sleep(1)
            motor1.set_duty_cycle(-60)
            utime.sleep(1)
            motor1.set_duty_cycle(-100)
            utime.sleep(1)
            motor1.set_duty_cycle(-120)
            utime.sleep(1)
            motor1.set_duty_cycle(0)
            utime.sleep(1)

    except(KeyboardInterrupt):
        print("Program Terminated")