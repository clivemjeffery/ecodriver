class PiGlowLights:
	def __init__(self):
		self.leds = []
		for x in range(18):
			self.leds.append(0)
			
	def all_off(self):
		return self.leds
		
	def all_on(self, value):
		leds_on = []
		for x in range(18):
			leds_on.append(value)
		return leds_on
		
	def some_on(self, value):
		leds_on = []
		for x in range(18):
			if (x % 2) == 0:
				leds_on.append(value)
			else:
				leds_on.append(0)
		return leds_on
		
	def one_on(self, led, value):
		led_on = list(self.leds)
		if led > 0:
			if led < 18:
				led_on[led - 1] = value
		return led_on
		
	def red_on(self, value):
		leds_on = list(self.leds)
		leds_on[0] = leds_on[6] = leds_on[17] = value
		return leds_on
		
	def orange_on(self, value):
		leds_on = list(self.leds)
		leds_on[1] = leds_on[7] = leds_on[16] = value
		return leds_on
		
	def yellow_on(self, value):
		leds_on = list(self.leds)
		leds_on[2] = leds_on[8] = leds_on[15] = value
		return leds_on
		
	def green_on(self, value):
		leds_on = list(self.leds)
		leds_on[3] = leds_on[5] = leds_on[13] = value
		return leds_on
		
	def blue_on(self, value):
		leds_on = list(self.leds)
		leds_on[4] = leds_on[11] = leds_on[14] = value
		return leds_on
		
	def white_on(self, value):
		leds_on = list(self.leds)
		leds_on[9] = leds_on[10] = leds_on[12] = value
		return leds_on
