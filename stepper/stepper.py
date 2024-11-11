import spidev
import RPi.GPIO as GPIO
import time

# Setup the CS pin for each Arduino
CS_pins = [8, 7, 25]  # Example GPIO pins for CS lines

def select_slave(pin):
    GPIO.output(pin, GPIO.LOW)

def deselect_slave(pin):
    GPIO.output(pin, GPIO.HIGH)

# Initialize SPI and GPIO
spi = spidev.SpiDev()
spi.open(0, 0)  # SPI bus 0, device 0
spi.max_speed_hz = 1000000  # 1 MHz communication speed

GPIO.setmode(GPIO.BCM)
for pin in CS_pins:
    GPIO.setup(pin, GPIO.OUT)
    deselect_slave(pin)

try:
    while True:
        for i, pin in enumerate(CS_pins):
            select_slave(pin)
            response = spi.xfer2([0x01, 0x02])  # Send dummy data to Arduino
            print(f"Response from Arduino {i}: {response}")
            deselect_slave(pin)
            time.sleep(1)

except KeyboardInterrupt:
    spi.close()
    GPIO.cleanup()
