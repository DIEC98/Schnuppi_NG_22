from machine import ADC
from machine import Pin
import time

def read_ADC_Val():
    while True:
        pin27 = Pin(27, Pin.IN)
        adc = ADC(pin27)
        
        val = adc.read_u16()
        val2 = adc.read_uv()
        
        print(val)
        print(val2)
        
        time.sleep(1)
        
read_ADC_Val()