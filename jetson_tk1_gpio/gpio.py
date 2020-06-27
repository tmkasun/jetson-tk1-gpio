import os
import time


class GPIO(object):
    # sysfs root
    _SYSFS_ROOT = "/sys/class/gpio"
    OUT = 1
    IN = 0
    HIGH = True
    LOW = False

    def __init__(self, pin, mode=None, initialOutput=False):
        super().__init__()
        self.pin = pin
        self.mode = mode
        self.output = initialOutput

    def setOutput(self, level):
        self.output = level
        if not self.isExported():
            raise RuntimeError(
                "ERROR: You need to setup the GPIO pin (export) before seting the output!!!")
        gpio_value_path = GPIO._SYSFS_ROOT + "/gpio%i" % self.pin + "/value"
        while not os.access(gpio_value_path, os.R_OK | os.W_OK):
            print("DEBUG: Waiting for permission [setOutput] . . .")
            time.sleep(0.01)
        with open(gpio_value_path, 'w') as value_file:
            if self.output is GPIO.LOW:
                value_file.write("0")
            elif self.output is GPIO.HIGH:
                value_file.write("1")

    def getOutput(self):
        if not self.isExported():
            raise RuntimeError(
                "ERROR: You need to setup the GPIO pin (export) before reading the output!!!")
        gpio_value_path = GPIO._SYSFS_ROOT + "/gpio%i" % self.pin + "/value"
        output_value = None
        with open(gpio_value_path, 'r') as value_file:
            output_value = value_file.read()
        return output_value

    def isExported(self):
        return os.path.exists(GPIO._SYSFS_ROOT + "/gpio%i" % self.pin)

    def setup(self):
        if (not os.access(GPIO._SYSFS_ROOT + '/export', os.W_OK) or
                not os.access(GPIO._SYSFS_ROOT + '/unexport', os.W_OK)):
            raise RuntimeError("The current user does not have permissions set to "
                               "access the library functionalities. Please configure "
                               "permissions or use the root user to run this")
        if self.isExported():
            print("WARNING: Pin has already exported!\nSkipping exporting . . .")
        else:
            gpio_export_path = "{root}/export".format(root=GPIO._SYSFS_ROOT)
            with open(gpio_export_path, 'w') as export_file:
                export_file.write(str(self.pin))
        if not self.mode:
            raise RuntimeError(
                "GPIO pin mode is not set, Please set the pin mode as GPIO.OUT or GPIO.IN to setup the pin")
        self.setMode(self.mode)

    def setMode(self, mode):
        self.mode = mode
        if not self.isExported():
            print(
                "WARNING: You haven't setup the GPIO pin (export) yet, Skiping writing mode to sysfs!")
            return
        gpio_direction_path = GPIO._SYSFS_ROOT + "/gpio%i" % self.pin + "/direction"
        while not os.access(gpio_direction_path, os.R_OK | os.W_OK):
            print("DEBUG: Waiting for permission [setMode] . . .")
            time.sleep(0.01)
        with open(gpio_direction_path, 'w') as direction_file:
            if self.mode is GPIO.OUT:
                direction_file.write("out")
            elif self.mode is GPIO.IN:
                direction_file.write("in")

    def getMode(self):
        pass

    """
        Do not support PWM or Events
    """

    def cleanup(self):
        with open("{root}/unexport".format(root=GPIO._SYSFS_ROOT), 'w') as unexport_file:
            unexport_file.write(str(self.pin))

    def debug(self):
        try:
            with open("/sys/kernel/debug/gpio", 'r') as debug_file:
                print(debug_file.read())
        except PermissionError as perError:
            print("ERROR: Do not have permission to access GPIO debug!!")
        print("DEBUG: Pin number = {}".format(self.pin))
        print("DEBUG: Mode = {}".format(self.mode))
        print("DEBUG: Output = {}".format(self.output))
