import RPi.GPIO as GPIO
import sys
import os
from subprocess import Popen
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
movie1 = ("/home/pi/Videos/dancehall_video.mp4")
last_state1 = False
input_state1 = False
player = False



while True:
    #Read states of inputs
    input_state1 = GPIO.input(17)

    print input_state1
    #If GPIO(17) is shorted to ground
    if input_state1 != last_state1:
        if player:
            os.system('killall omxplayer.bin')
        if input_state1:
            omxc = Popen(['omxplayer', '-b', '--win','0 50 690 480', movie1])
            player = True
            time.sleep(98)
            
        

    #Set last_input states
    last_state1 = input_state1
