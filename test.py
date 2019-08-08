import time
import gpio


gpio.setup_gpio(21, 'out')
while 1:
    gpio.set_value(21, 1)
    time.sleep(0.1)
    gpio.set_value(21, 0)
    time.sleep(0.1)