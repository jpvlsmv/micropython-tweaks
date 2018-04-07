def main():
    """Entry point for the application script"""
    print("Call your main application code here")

def pulse(pin, t):
        import time, math
	from machine import PWM
	p = PWM(pin, freq=1000)
	for i in range(20):
		p.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
		time.sleep_ms(t)
	p.deinit()

# Utility functions
def cat(x):
        import uio
	print(uio.open(x).read())

def noexport():
	print("This is not exported from the module")

# __name__ = "jfm" #(vs micropython-jfm)

if __name__ != "__main__":
	__all__ = [ "pulse", "cat" ]
