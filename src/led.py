"""! @file led.py
This program controls the brightness of an LED using a PWM signal
sent over pin PAO.
"""

import utime
import pyb
import micropython
micropython.alloc_emergency_exception_buf(100)

def led_setup ():
    """!
    Sets up two timer channels for both the PWM at PA0 and LED callback,
    respectively. 
    """
    global ch1
    global tim1
    global dty
    
    pinA0 = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
    tim2 = pyb.Timer(2, freq=20000)
    ch1 = tim2.channel(1, pyb.Timer.PWM_INVERTED, pin=pinA0)
    
    tim1 = pyb.Timer(1, freq = 20)
    tim1.callback(led_brightness)
    
    dty = 100

def led_brightness (tim_num):
    """!
    Decreases LED brightness by adjusting PWM Duty Cycle
    from 100% to 0% using Callback Method.
    """
    global ch1
    global dty
    
    if (dty == 0 ):
        dty = 100
    dty -= 1
    
    ch1.pulse_width_percent(dty)
    
if __name__ == "__main__":
    try:
        led_setup()
        
        while True:
            continue

    except(KeyboardInterrupt):
        tim1.callback(None)
        print("Program Terminated")
        
