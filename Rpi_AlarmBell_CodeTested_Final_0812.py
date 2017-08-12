import time
import RPi.GPIO as GPIO
import os # to set the timezone

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)

FlagStartCounter = 0
os.environ['TZ'] ='Africa/Kigali' #change this according to the timezone you are in
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
    if (t[3] == 7 and t[4] == 35 and t[5] == 0) is True: # start time for 7.35am. Change this value according to the time you want to start the bell
        GPIO.output(3, True) # ring the alarm at the start
        print (t)
        hour = t[3]
        minutes = t[4]
        seconds = t[5]
        FlagStartCounter = True
        break
    else:
        FlagStartCounter = False

while FlagStartCounter is True:
    time.sleep(600) # check time every 10 min = 600sec
    t = time.localtime()
    if ((t[3] - hour is 1) and (abs(t[4] - minutes) < 5)): 
        GPIO.output(3, True) # ring the alarm
        hour = t[3]
        minutes = t[4]
        t = time.localtime()
        print(t)
    else:
        GPIO.output(3, False)
        
        
        
        
