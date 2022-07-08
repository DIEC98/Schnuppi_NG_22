# Carl Dietzel 1.7.22

from machine import Pin
import machine
import time, math

pin = Pin(33,Pin.OUT)
pin2 = Pin(25, Pin.OUT)
pin3 = Pin(32, Pin.OUT)

def blink_led():
    
    for x in range(2,6):
        pin.on()
        time.sleep(1)
        pin.off()
        time.sleep(1)
        
def fade_led(pin, pin2, pin3, duty, freq):
    
    pwm_led = machine.PWM(pin) 
    pwm_led.freq(freq)
    pwm_led.duty(duty)
    
    pwm_led = machine.PWM(pin2) 
    pwm_led.freq(freq)
    pwm_led.duty(duty)
    
    pwm_led = machine.PWM(pin3) 
    pwm_led.freq(freq)
    pwm_led.duty(duty)

    
def main():
    freq = 100
    duty = 0
    while True:
        fade_led(pin, pin2, pin3, duty, freq)
        
        if duty is  0:
            math = 1
        if duty is 330:
            math = 0
            
        if math is 1: #addition
            duty += 10
        if math is 0: #subtraktion
            duty -= 10
            
        time.sleep_ms(100)
     
main()    
