#!/usr/bin/env python3
import subprocess
import os
import time

# https://elinux.org/Jetson/Thermal
#https://elinux.org/Jetson/Tutorials/GPIO

def initGPIO(port=57):
	subprocess.call(["echo", port, ">" ,"/sys/class/gpio/export"])
	subprocess.call(["echo", "out", ">" ,"/sys/class/gpio/gpio{}/direction".format(port)])

def switchOn(state="1",port=57):
	os.system("echo {} > /sys/class/gpio/gpio{}/value".format(state,port))

def getSwitchState(port=57):
	subprocess.call(["cat", "/sys/class/gpio/gpio{}/value".format(port)])


def main():
	print("Starting A/C Controller")
	#switchOn("0")
	#return
	while True:
		print("Turning on")
		# 165
		switchOn("1")
		time.sleep(60*2)
		print("Turning off")
		switchOn("0")
		time.sleep(60*3)


if __name__ == "__main__":
	main()

