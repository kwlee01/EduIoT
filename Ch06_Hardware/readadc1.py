from gpiozero import MCP3008
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setwarnings(False)

while True:
	pot=MCP3008(0)
	val=pot.value*3.3
	print(val)
	if (val>2.0):
		GPIO.output(21,True)
	else:	
		GPIO.output(21,False)
	
	#print(pot.value*3.3)
	time.sleep(1)
GPIO.cleanup()
