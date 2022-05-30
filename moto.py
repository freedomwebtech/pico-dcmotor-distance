from machine import Pin
import utime



p = machine.PWM(machine.Pin(2))
p1 = machine.PWM(machine.Pin(3))
p.freq(1000)
while True:
    a=input("enter:-")
    b=int(str(a))
    p.duty_u16(b)
