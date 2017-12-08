import sys
import Adafruit_DHT as reader


class Sensor():


    def __init__(self):
        self.__sensor = 11
        self.__pin = 4

    
    def read(self):
        return reader.read_retry(self.__sensor,self.__pin)
        

