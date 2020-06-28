# Intro

This is a python library for interacting with Nvidia Jetson TK1 GPIO. This library is specifically for Jetson TK1 and not for others, If you are looking for a GPIO library for other Jetson variant checkout [this repository](https://github.com/NVIDIA/jetson-gpio/)

I have built this around the `sysfs` interface for GPIO's and inpired by the NVIDIA's official GPIO library for TX1, TX2, Nano etc Jetson versions.

# Setup file system permission

Please follow the guide in [NVIDIA/Jetson-GPIO readme](https://github.com/NVIDIA/jetson-gpio#setting-user-permissions) to setup file system permissions

# Usage

This library provides a `GPIO` class definition which you can create gpio objects out of that, An instance work as one GPIO pin and you can, setup, set data flow direction(mode), output status that is, if out direction whther output needs to be high(~1.8v) or low(~0.0v) etc and finaly cleanup the GPIO pin(unexport).

- To initialize a GPIO pin (Create an GPIO object), You need to provide, `sysfs filename` number (i:e if gpio165 give `165`) as the first argument, and the mode (direction) and optionaly you can provide the output initial state

|      Port      |sysfs filename                 |Physical pin                                       |
|----------------|-------------------------------|---------------------------------------------------|
| GPIO_PH1       | gpio57                        |	Pin 50 on J3A1                                   |
| GPIO_PU6       | gpio166                       |	Pin 58 on J3A2                                   |
| GPIO_PU5       | gpio165                       |	Pin 55 on J3A2                                   |
| GPIO_PU4       | gpio164                       |	Pin 52 on J3A2                                   |
| GPIO_PU3       | gpio163                       |	Pin 49 on J3A2                                   |
| GPIO_PU2       | gpio162                       |	Pin 46 on J3A2 (Disabled by default)             |
| GPIO_PU1       | gpio161                       |	Pin 43 on J3A2                                   |
| GPIO_PU0       | gpio160                       |	Pin 40 on J3A2                                   |

~[Source](https://elinux.org/Jetson/GPIO)

```python
  fan = GPIO(165,GPIO.OUT)
```

- Setup pin, This call will export the pin and set the direction as well (if direction is given when creating the GPIO object)

```python
  fan.setup()
```

- Debug the pin, If `/sys/kernel/debug/gpio` is assessable, Will print the content of it , else will print the object properties

```python
  fan.debug()
```

- Set output, Set the output of the pin either `GPIO.HIGH` or `GPIO.LOW`

```python
fan.setOutput(GPIO.HIGH)
```
- Cleanup after all, Will `unexport` the pin from `sysfs`
```python
fan.cleanup()
```
# Warning

This is in very early stage of development , and not intended to be used in any serious work :)
