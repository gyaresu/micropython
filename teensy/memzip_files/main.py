import pyb
print("Executing main.py")

led = pyb.LED(1)

def blinken(n):
    for m in range(1, n):
        led.on()
        pyb.delay(100)
        led.off()
        pyb.delay(100)
        led.on()
        pyb.delay(100)
        led.off()
    print("End of script")




