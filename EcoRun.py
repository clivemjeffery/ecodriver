#
# EcoRun.py
# 	This is a testing version of the eCoDriver program. It runs in X with some on screen instruments
#	that help me to show the children what information the XLoBorg is giving us. They understand that
#	the sensors detect force and can see that the force of gravity pulls *down* on the board is 1G.
#	When we shake the Pi (and XLoBorg) vigorously, they can see the force measurements in the x and y
#	axes. We also used this to choose which acceleration axis to control the lights from.
#
#	From their understanding of programming the PiGlow in Scratch GPIO, they have contributed to the
#	parts of the code that turn lights on depending on the level of the x acceleration. See comments.
#
import EcoDriver as ed		# This module hides the complex Tkinter code to show the instruments
import XLoBorg as xlo		# This module lets us read from the XLoBorg. PiBorg made it.
import piglow as piglow		# This one lets us turn on PiGlow lights. Pimoroni made ti.
import piglowlights as pgl	# This makes the lights easier to use the way we want. Mr Jeffery made it.
from math import *

TIMED_ACTION_INTERVAL = 1000 # milliseconds
pg = piglow.PiGlow()
l = pgl.PiGlowLights()

#
# We will run this function 'readXlo' every interval (see TIMED_ACTION_INTERVAL) to read the
# accelerometer values and then control the PiGlow lights.
#
def readXlo():
	ax, ay, az = xlo.ReadAccelerometer()
	
	app.instAccelX.acceleration.set(ax)	# set the screen instruments
	app.instAccelY.acceleration.set(ay)
	app.instAccelZ.acceleration.set(az)

	# Turn on PiGlow lights to show how much x acceleration there is.
	# This part is where the children have helped to code in python ---------------
	if ax > 0.5:
		pg.update_leds(l.red_on(255))
		pg.update_leds(l.orange_on(50))
		pg.update_leds(l.yellow_on(20))
	elif ax > 0.45:
		pg.update_leds(l.red_on(100))
		pg.update_leds(l.orange_on(255))
		pg.update_leds(l.yellow_on(40))
	elif ax > 0.4:
		pg.update_leds(l.red_on(20))
		pg.update_leds(l.orange_on(100))
		pg.update_leds(l.yellow_on(50))
	elif ax > 0.3:
		pg.update_leds(l.orange_on(50))
		pg.update_leds(l.yellow_on(100))
		pg.update_leds(l.green_on(5))
	elif ax > 0.2:
		pg.update_leds(l.yellow_on(100))
		pg.update_leds(l.green_on(10))
	elif ax > 0.15:
		pg.update_leds(l.yellow_on(20))
		pg.update_leds(l.green_on(20))
	else:
		pg.update_leds(l.green_on(20))
	#------------------------------------------------------------------------------
	app.setTimedActions(readXlo, TIMED_ACTION_INTERVAL) # make sure to call again

# Start the App! This is the first sectio of code that runs when we launch this
# script with python. It creates the app, sets the name of the procedure with the
# timed actions we want and then runs the app's main loop. The main loop will call
# our timed actions every TIMED_ACTION_INTERVAL (milliseconds)
#
xlo.printFunction = xlo.NoPrint
xlo.Init()
app = ed.EcoDriverApp()
app.setTimedActions(readXlo, TIMED_ACTION_INTERVAL)
app.mainloop()
pg.update_leds(l.all_off())
