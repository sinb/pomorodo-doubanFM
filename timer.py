# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 14:09:48 2015

@author: hehe
"""
import subprocess
import os
import random
def sec2time(seconds):
    """convert python seconds to min : sec
    """
    mins = seconds / 60;
    secs = seconds % 60;
    return str("%02d" % mins) + ' : ' + str("%02d" % secs)

def getPlayList(music_dir):
    """grab all the mp3 file in the folder
    Put them to a list
    """
    playList = []
    for (dirname, dirs, files) in os.walk(music_dir):
        for file in files:
            if file.endswith('.mp3'):
                thefile = os.path.join(dirname, file)
                playList.append(thefile)
    return playList               

def playRandomSong(List):
    """randomly choose a form list to play
    """
    idx = random.randint(0, len(List)-1)
    songName = List[idx]
    child = subprocess.Popen(['mpg123', '-q', List[idx]])
    return child, songName
def playWorkSong():
    """play "work work" at the begining
    """
    child = subprocess.Popen(['mpg123', '-q', os.path.dirname(os.path.realpath(__file__))+"/data/work.mp3"])
    return child    