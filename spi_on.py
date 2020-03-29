#! /usr/bin/env python

import pyftdi.spi
import time

spi = pyftdi.spi.SpiController()
spi.configure('ftdi:///1')
gpio = spi.get_gpio();
gpio.set_direction(0x0100, 0x0100)
gpio.write(0x0000)
time.sleep(0.100)
gpio.write(0x0100)
