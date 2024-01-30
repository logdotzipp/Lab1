"""! @file led.py
This program controls the brightness of an LED using a PWM signal
sent over pin PAO.
"""

import utime
import pyb

def led_setup ():
    """! Doxygen style docstring for this function """
    global ch1
    pinA0 = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
    tim2 = pyb.Timer(2, freq=20000)
    ch1 = tim2.channel(1, pyb.Timer.PWM_INVERTED, pin=pinA0)
    
    timmy = pyb.Timer(1, freq = 20)
    timmy.counter ()
    timmy.callback(led_brightness)
    
    global dty
    dty = 100
    return ch1

def led_brightness (tim_num):
    """! Doxygen style docstring for this function """
    global ch1
    global dty
    
    if (dty == 0 ):
        dty = 100
    dty -= 1
    
    ch1.pulse_width_percent(dty)

if __name__ == "__main__":
    try:
        ch1 = led_setup()
        
        while True:
            continue

    except(KeyboardInterrupt):
        print("Program Terminated")
        
