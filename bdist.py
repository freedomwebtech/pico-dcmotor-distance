import hcsr04
from time import sleep
ultrasonic=hcsr04.HCSR04(trigger_pin=27,echo_pin=26,echo_timeout_us=1000000)
while True:
    a=ultrasonic.distance_cm()
    sleep(0.1)
    print(a)
