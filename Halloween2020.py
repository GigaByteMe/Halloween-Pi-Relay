# Raspberry pi motion detection
# This code was taken from multiple different sites and spaces.
# there is code to make the PIR Sensor work, code that makes the pygame 
# sound play, and code to make the Relays work.  I have taken bits and pieces
# from all of these and created this ... Frankenstein's Monster if you will
# Enjoy!

import os, pygame, time, random
import RPi.GPIO as GPIO # setup GPIO board

pygame.mixer.init()

SENSOR_PIN = 23
counter = 0

GPIO.setmode(GPIO.BCM)
# Setup Sesnor PINS
GPIO.setup(SENSOR_PIN, GPIO.IN)

# Setup Relay PINS
# Only using 2 at this time, so commenting out 1 & 2 only use relay 3
#GPIO.setup(26, GPIO.OUT) # -- BCM Pin 26 - Wiring Pi Pin 25 - Pysical pin 37 - Relay #2
#GPIO.setup(20, GPIO.OUT) # -- BCM Pin 20 - Wiring Pi Pin 28 - Pysical pin 38 - Relay #1 
GPIO.setup(21, GPIO.OUT)  # -- BCM Pin 21 - Wiring Pi Pin 29 - Pysical pin 40 - Relay #3

# Set Relay to Closed
#GPIO.output (26, True)
#GPIO.output (20, True)
GPIO.output (21, True)

try:
	while True:
		if GPIO.input(23): #Check for input on pin23
			# We HAVE MOVEMENT!
			# Get a random sound
			num = random.randint(1,4)

			# Play Scary Sound
			pygame.mixer.music.load("/home/pi/Music/sound-effect-" + str(num) + ".mp3")
			pygame.mixer.music.play()
			# For Debugging
			#print ("Sound = sound-effect-" + str(num))
			
			# HIT THE LIGHTS!
			#GPIO.output (26, False)
			#time.sleep(0.25) #give them a second 
			#GPIO.output (20, False)
			#time.sleep(0.25) #give them a second 
			GPIO.output (21, False)
			time.sleep(5) 

			# Lights Out
			#GPIO.output (26, True)
			#GPIO.output (20, True)
			GPIO.output (21, True)
						
			# Finish up for longer sounds
			# and a small reset, so it's not going off constantly
			time.sleep(2) 
finally:
	GPIO.cleanup()
