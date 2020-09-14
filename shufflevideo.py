#!/usr/bin/env python2
import gpiozero
import sys
import os
from subprocess import Popen
import time
import random

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
movie20 = ("/home/pi/Videos/video20.mp4")
movie21 = ("/home/pi/Videos/video21.mp4")
movie22 = ("/home/pi/Videos/video22.mp4")
movie23 = ("/home/pi/Videos/video23.mp4")
movie24 = ("/home/pi/Videos/video24.mp4")
movie25 = ("/home/pi/Videos/video25.mp4")
movie26 = ("/home/pi/Videos/video26.mp4")
movie27 = ("/home/pi/Videos/video27.mp4")
movie28 = ("/home/pi/Videos/video28.mp4")
movie29 = ("/home/pi/Videos/video29.mp4")
movie30 = ("/home/pi/Videos/video30.mp4")
movie31 = ("/home/pi/Videos/video31.mp4")
movie32 = ("/home/pi/Videos/video32.mp4")
movie33 = ("/home/pi/Videos/video33.mp4")
movie34 = ("/home/pi/Videos/video34.mp4")
movie35 = ("/home/pi/Videos/video35.mp4")
movie36 = ("/home/pi/Videos/video36.mp4")
movie37 = ("/home/pi/Videos/video37.mp4")
movie38 = ("/home/pi/Videos/video38.mp4")
movie39 = ("/home/pi/Videos/video39.mp4")
movie40 = ("/home/pi/Videos/video40.mp4")
movie41 = ("/home/pi/Videos/video41.mp4")
movie42 = ("/home/pi/Videos/video42.mp4")
movie43 = ("/home/pi/Videos/video43.mp4")
movie44 = ("/home/pi/Videos/video44.mp4")
movie45 = ("/home/pi/Videos/video45.mp4")
movie46 = ("/home/pi/Videos/video46.mp4")
movie47 = ("/home/pi/Videos/video47.mp4")
movie48 = ("/home/pi/Videos/video48.mp4")

movie_list = [movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10, movie11, movie12, movie13, movie14, movie15, movie16, movie17, movie18, movie19, movie20, movie21, movie22, movie23, movie24, movie25, movie26, movie27, movie28, movie29, movie30, movie31, movie32, movie33, movie34, movie35, movie36, movie37, movie38, movie39, movie40, movie41, movie42, movie43, movie44, movie45, movie46, movie47, movie48]

# Shuffle the movies, this modifies the list in-place
random.shuffle(movie_list)
print(movie_list)

null = open('/dev/null', 'w')

def button_handler(movie_list):
    omxc = [None]
    current_movie_no = [0]
    
    def button_handler_func():
        if omxc[0] and omxc[0].poll() is None:
            # may need kill() here instead of terminate()
            omxc[0].kill()
            omxc[0].wait()
            # expeiment with sleep time here; may not be needed
            time.sleep(1)
        else:
            # Increment the current movie. It's just an index into the
            # movie_list. Also, to keep it from being more than the
            # length of the movie_list, use "%" to wrap it back around
            # to 0. This is like a playlist on shuffle and repeat.
            current_movie_no[0] = (current_movie_no[0] + 1) % len(movie_list)
            current_movie = movie_list[current_movie_no[0]]
                
            omxc[0] = Popen(['omxplayer', '-o', 'local', '-b', '--win',
                             '-50 0 690 480', current_movie], stdout=null,
                            stderr=null)

    return button_handler_func

# experiment with hold time here
# also with bounce time
button = gpiozero.Button(pin=17, pull_up=False, hold_time=0.01, bounce_time=None)
button.when_pressed = button_handler(movie_list)

while(True):
    time.sleep(0.3)
    pass
