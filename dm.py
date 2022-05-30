import hcsr04
from machine import Pin
from time import sleep

p = machine.PWM(machine.Pin(2))
p1 = machine.PWM(machine.Pin(3))
p.freq(1000)

ultrasonic=hcsr04.HCSR04(trigger_pin=27,echo_pin=26,echo_timeout_us=1000000)
while True:
    a=ultrasonic.distance_cm()
    sleep(0.1)
    print(a)

    if a < 5:
       p.duty_u16(40000)
    elif 10< a < 50:
       p.duty_u16(60000)   
    else:
        p.duty_u16(0)
