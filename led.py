from gpiozero import LED, Button
from time import sleep

led = LED(27)
button = Button(2)

print('start')
for i in range(4):
    led.on()
    sleep(1)
    led.off()
    sleep(1)
print('stop')

while True:
    button.wait_for_press()
    led.on()
    sleep(1)
    led.off()