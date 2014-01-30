#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  PiGlowTest.py
#  
#  Copyright 2014  <pi@raspberrypi>
#  

import piglow as piglow
import piglowlights as pgl
from time import sleep

pg = piglow.PiGlow()
li = pgl.PiGlowLights()

def main():
	pg.update_leds(li.red_on(20))
	sleep(2)
	pg.update_leds(li.orange_on(20))
	sleep(2)
	pg.update_leds(li.yellow_on(20))
	sleep(2)
	pg.update_leds(li.green_on(20))
	sleep(2)
	pg.update_leds(li.blue_on(20))
	sleep(2)
	pg.update_leds(li.white_on(20))
	sleep(2)
	pg.update_leds(li.all_off())
	return 0

if __name__ == '__main__':
	main()

