# Sample script for PiGlow that creates a continuous whirly vortex animation
#
# Please see our GitHub repository for more information: https://github.com/pimoroni/piglow
#
# Once running you'll need to press ctrl-C to cancel stop the script

import time
from smbus import SMBus

# command register addresses for the SN3218 IC used in PiGlow
CMD_ENABLE_OUTPUT = 0x00
CMD_ENABLE_LEDS = 0x13
CMD_SET_PWM_VALUES = 0x01
CMD_UPDATE = 0x16

class PiGlow:
	i2c_addr = 0x54 # fixed i2c address of SN3218 ic
	bus = None

	def __init__(self, i2c_bus=1):
		self.bus = SMBus(i2c_bus)

        # first we tell the SN3218 to enable output (turn on)
		self.write_i2c(CMD_ENABLE_OUTPUT, 0x01)

        # then we ask it to enable each bank of LEDs (0-5, 6-11, and 12-17)
		self.write_i2c(CMD_ENABLE_LEDS, [0xFF, 0xFF, 0xFF])

	def update_leds(self, values):
		print "update pwm"
		self.write_i2c(CMD_SET_PWM_VALUES, values)
		self.write_i2c(CMD_UPDATE, 0xFF)

	# a helper that writes the given value or list of values to the SN3218 IC
	# over the i2c protocol
	def write_i2c(self, reg_addr, value):
        # if a single value is provided then wrap it in a list so we can treat
        # all writes in teh same way
		if not isinstance(value, list):
			value = [value];

        # write the data to the SN3218
		self.bus.write_i2c_block_data(self.i2c_addr, reg_addr, value)

# a list of 18 values between 0 - 255 that represent each LED on the PiGlow.
# to change the LEDs we set the values in this array and then pass it to the
# update_leds() function to actually update the LDEs
values = [0x01,0x02,0x04,0x08,0x10,0x18,0x20,0x30,0x40,0x50,0x60,0x70,0x80,0x90,0xA0,0xC0,0xE0,0xFF]
