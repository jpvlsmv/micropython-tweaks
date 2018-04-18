#!/usr/bin/env micropython
import utime
from machine import Pin

class sr04:
    def __init__(self, trig=None, echo=None, enable=False):
        '''Connect trig=machine.Pin(#) to SR-04 trigger and echo to SR-04 echo'''
        self.trig = trig
        self.echo = echo
    def enable(self):
        self.mailslot=0
        self.echo.irq(trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING, handler=self.sr04_irq)
    def disable(self):
        self.echo.irq(handler = None)
        self.mailslot=0
    def trigger(self):
        self.trig.value(1)
        usleep_ms(1) # FIXME: should be nonblocking
        self.trig.value(0)
    def get(self):
        while self.mailslot == 0:
            usleep_ms(1)
        return self.mailslot


    def sr04_irq(p):
        now = utime.ticks_us()
        if p.value() != 0:
            # edge has risen, start the clock
            self.mailslot=0
            self.lastup = now
        else
            self.mailslot = utime.ticks_diff(now, self.lastup)


lastup=utime.ticks_us()
trig = Pin(5,Pin.OUT)
echo = Pin(4,Pin.IN)
def sr04_irq(p):
    global lastup
    now = utime.ticks_us()
    if p.value() != 0:
        #Risen edge
        lastup = now
    else:
        print(utime.ticks_diff(now,lastup))
def sr04_init():
    global trig,echo
    echo.irq(trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING, handler=sr04_irq)
def sr04_trig():
    global trig
    trig.value(1) ; utime.sleep_us(10) ; trig.value(0)
