import RPi.GPIO as gpio
import time


class Motors(): 
    gpio.setwarnings(False)

    def __init__(self):
        self.__pins_used = [6,13,16,19,20,26]
        self.__Enable_motor_1 = 19
        self.__Enable_motor_2 = 26
        self.__Motor_1_Forward = 6
        self.__Motor_1_Reverse = 13
        self.__Motor_2_Forward = 16
        self.__Motor_2_Reverse = 20
        '''
EnableA - 19
EnableB - 26
IN1 - 6
IN2 - 13
IN3 - 16
IN4 - 20
        ''' 
        
        
        gpio.setmode(gpio.BCM)
        for i in self.__pins_used:
            gpio.setup(i, gpio.OUT)

    def init(self):
        self.__pins_used = [6,13,16,19,20,26]
        self.__Enable_motor_1 = 19
        self.__Enable_motor_2 = 26
        self.__Motor_1_Forward = 6
        self.__Motor_1_Reverse = 13
        self.__Motor_2_Forward = 16
        self.__Motor_2_Reverse = 20
        
        gpio.setmode(gpio.BCM)
        for i in self.__pins_used:
            gpio.setup(i, gpio.OUT)


    def stop(self):
        print "stop"
        
        gpio.output(self.__Enable_motor_1, True) 
        gpio.output(self.__Enable_motor_2, True)
        gpio.output(self.__Motor_1_Forward, False) 
        gpio.output(self.__Motor_2_Forward, False)
    
        gpio.output(self.__Motor_1_Reverse, False)
        gpio.output(self.__Motor_2_Reverse, False)

    def forward(self):
        print "Forward"
        
        gpio.output(self.__Enable_motor_1, True) 
        gpio.output(self.__Enable_motor_2, True)
        gpio.output(self.__Motor_1_Forward, True) 
        gpio.output(self.__Motor_2_Forward, True)
    
        gpio.output(self.__Motor_1_Reverse, False)
        gpio.output(self.__Motor_2_Reverse, False)


    def reverse(self):
        print "Reverse"
        
        gpio.output(self.__Enable_motor_1, True) 
        gpio.output(self.__Enable_motor_2, True)
        gpio.output(self.__Motor_1_Forward, False) 
        gpio.output(self.__Motor_2_Forward, False)
    
        gpio.output(self.__Motor_1_Reverse, True)
        gpio.output(self.__Motor_2_Reverse, True)

      

    def left(self):
        print "Left"
        
        gpio.output(self.__Enable_motor_1, True) 
        gpio.output(self.__Enable_motor_2, True)
        gpio.output(self.__Motor_1_Forward, True) 
        gpio.output(self.__Motor_2_Forward, False)
    
        gpio.output(self.__Motor_1_Reverse, False)
        gpio.output(self.__Motor_2_Reverse, True)
    


    def right(self):
        print "Right"
        
        gpio.output(self.__Enable_motor_1, True) 
        gpio.output(self.__Enable_motor_2, True)
        gpio.output(self.__Motor_1_Forward, False) 
        gpio.output(self.__Motor_2_Forward, True)
    
        gpio.output(self.__Motor_1_Reverse, True)
        gpio.output(self.__Motor_2_Reverse, False)
    

        
    def _deinit_(self):
        gpio.cleanup()

