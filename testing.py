#!/usr/bin/env python3
import time

from jetson_tk1_gpio.gpio import GPIO

# https://elinux.org/Jetson/Thermal
# https://elinux.org/Jetson/Tutorials/GPIO

def main():
	print("GPIO Testing")
	fan = GPIO(165,GPIO.OUT)
	fan.setup()
	fan.debug()
	fan.setOutput(GPIO.HIGH)
	time.sleep(2)
	fan.setOutput(GPIO.LOW)
	fan.cleanup()

if __name__ == "__main__":
	main()