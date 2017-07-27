import time
import RPi.GPIO as GPIO
import os # to set the timezone

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)

FlagStartCounter = 0
os.environ['TZ'] = 'Africa/Kigali'
time.tzset()
''' for reference
year = t[0]
day = t[1]
month = t[2]
hour = t[3]
minutes = t[4]
seconds = t[5]
'''

while True:
	t = time.localtime()
	if (t[3] == 7 and t[4] == 35 and t[5] == 0) is True: # start time for 7.35am
		GPIO.output(3, True) # ring the bell at start
		print (t)
		hour = t[3]
		minutes = t[4]
		seconds = t[5]
		FlagStartCounter = True
		break
	else:
		FlagStartCounter = False

while FlagStartCounter is True:
	time.sleep(1200) # check every 20 minutes = 1200 seconds
	t = time.localtime()
	if t[4] - minutes is 60:
		GPIO.output(3, True) # activate alarm every 60 minutes
		minutes = t[4]
		t = time.localtime()
		print (t)
	else:
		GPIO.output(3, False)
	
		