import utime
from machine import Pin
lastup=utime.ticks_us()
trig = Pin(5,Pin.OUT)
echo = Pin(4,Pin.IN)
def sr04_irq(p):
    global lastup
    now = utime.ticks_us()
    flags = p.irq().flags()
    if flags & Pin.IRQ_RISING:
        lastup = now
    else:
        print(utime.ticks_diff(now,lastup))
def sr04_init():
    global trig,echo
    echo.irq(trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING, handler=sr04_irq)
def sr04_trig():
    global trig
    trig.value(1) ; utime.sleep_us(10) ; trig.value(0)
