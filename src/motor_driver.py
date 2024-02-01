
import pyb
import micropython

class MotorDriver:
    """! 
    This class implements a motor driver for an ME405 kit. 
    """

    def __init__ (self, en_pin, in1pin, in2pin, timer):
        """! 
        Creates a motor driver by initializing GPIO
        pins and turning off the motor for safety. 
        @param en_pin Pin in the pyboard that enables the motor.
        @param in1pin First pin used for input to Motor's H-bridge.
        @param in2pin Second pin used for input to Motor's H-bridge.
        @param timer Timer channel used to drive PWM.
        """
        print ("Creating a motor driver")
        
        self.pinEN = pyb.Pin(en_pin, pyb.Pin.OUT_OD, pyb.Pin.PULL_UP)
        self.pinEN.value(0)
    
        pinIN1A = pyb.Pin(in1pin, pyb.Pin.OUT_PP)
        pinIN2A = pyb.Pin(in2pin, pyb.Pin.OUT_PP)
    
    # Setup PWM Timers
        #tim3 = pyb.Timer(3, freq=20000)
        self.chIN1A = timer.channel(1, pyb.Timer.PWM, pin=pinIN1A)
        self.chIN2A = timer.channel(2, pyb.Timer.PWM, pin=pinIN2A)
        
        

    def set_duty_cycle (self, level):
        """!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        """
        print (f"Setting duty cycle to {level}")
        
        if level >= 0:
            # Forward Direction
            if level > 100:
                level = 100
            
            self.pinEN.value(1) # Enable motor
        
            self.chIN1A.pulse_width_percent(0)
            self.chIN2A.pulse_width_percent(level)
            
        else:
            # Backwards Direction
            if level < -100:
                level = -100
            
            self.pinEN.value(1) # Enable motor
        
            self.chIN1A.pulse_width_percent(abs(level))
            self.chIN2A.pulse_width_percent(0)
            
# if __name__ == "__main__":
#     try:
#         motor1 = MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, pyb.Timer(3, freq=20000))
#         
#         while True:
#             motor1.set_duty_cycle(30)
#       
#         
#     except(KeyboardInterrupt):
#         print("Program Terminated")
            