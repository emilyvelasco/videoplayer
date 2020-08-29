import RPi.GPIO as GPIO
import sys
import os
from subprocess import Popen
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
movie1 = ("/home/pi/Videos/video1.mp4")
movie2 = ("/home/pi/Videos/video2.mp4")
movie3 = ("/home/pi/Videos/video3.mp4")
movie4 = ("/home/pi/Videos/video4.mp4")
movie5 = ("/home/pi/Videos/video5.mp4")
movie6 = ("/home/pi/Videos/video6.mp4")
movie7 = ("/home/pi/Videos/video7.mp4")
movie8 = ("/home/pi/Videos/video8.mp4")
movie9 = ("/home/pi/Videos/video9.mp4")
movie10 = ("/home/pi/Videos/video10.mp4")
movie11 = ("/home/pi/Videos/video11.mp4")
movie12 = ("/home/pi/Videos/video12.mp4")
movie13 = ("/home/pi/Videos/video13.mp4")
movie14 = ("/home/pi/Videos/video14.mp4")
movie15 = ("/home/pi/Videos/video15.mp4")
movie16 = ("/home/pi/Videos/video16.mp4")
movie17 = ("/home/pi/Videos/video17.mp4")
movie18 = ("/home/pi/Videos/video18.mp4")
movie19 = ("/home/pi/Videos/video19.mp4")
last_state1 = False
input_state1 = False
player = False
movie_list = [movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10, movie11, movie12, movie13, movie14, movie15, movie16, movie17, movie18, movie19]

# Shuffle the movies, this modifies the list in-place
random.shuffle(movie_list)
current_movie_no = 0


while True:
    #Read states of inputs
    input_state1 = GPIO.input(17)

    print input_state1
    #If GPIO(17) is shorted to ground
    if input_state1 != last_state1:
        if player:
            os.system('killall omxplayer.bin')
        if input_state1:
            # Increment the current movie. It's just an index into the
            # movie_list. Also, to keep it from being more than the
            # length of the movie_list, use "%" to wrap it back around
            # to 0. This is like a playlist on shuffle and repeat.
            current_movie_no = (current_movie_no + 1) % len(movie_list)
            current_movie = movie_list[current_movie_no]

            omxc = Popen(['omxplayer', '-b', '--win','0 50 690 480', current_movie])
            player = True
            time.sleep(98)
            
        

    #Set last_input states
    last_state1 = input_state1
