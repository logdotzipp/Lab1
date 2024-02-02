"""! @file led.py
This program controls the brightness of an LED using a PWM signal
sent over pin PAO. The LED grows in brightness from 0% to 100% over 5
seconds, and then drops back down to 0%. It then cycles indefinitely.
"""

import utime
import pyb
import micropython
micropython.alloc_emergency_exception_buf(100)

def led_setup ():
    """!
    Sets up two timer channels for both the PWM at PA0 and LED callback,
    respectively.
    @param ch1 Timer channel associated with GPIO PA0.
    @param tim2 Timer associated with GPIO PA0.
    @param tim1 Timer Channel Callback used for updating the brightness of the LED over time.
    @param dty Duty Cycle percent used to change LED brightness.
    """
    global ch1
    global tim1
    global dty
    
    # Set up pin A0 as an output
    pinA0 = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
    # Set up a timer for running PWM output to the LED
    tim2 = pyb.Timer(2, freq=20000)
    # Set up a PWM channel for the LED
    ch1 = tim2.channel(1, pyb.Timer.PWM_INVERTED, pin=pinA0)
    
    # Create a timer for updating the LED brightness
    tim1 = pyb.Timer(1, freq = 20)
    tim1.callback(led_brightness)
    
    # Set the initial value of the LED to 100, which corresponds to 0% brightness
    dty = 100

def led_brightness (tim_num):
    """!
    Increases the LED brightness by adjusting PWM Duty Cycle
    from 0% to 100% on a 20Hz timer. This results in a full 0-100 cycle over 5 seconds.
    """
    global ch1
    global dty
    
    # If dty has reached 0 (100% brightness) change it to 100 (0% brightness)
    if (dty == 0 ):
        dty = 100
    # Decrement dty (Increase brightness one tick)
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
        
