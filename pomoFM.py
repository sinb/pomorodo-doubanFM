# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 14:09:48 2015

@author: hehe
"""
import json
import subprocess
import os
import random
import time
import sys
from doubanapi import *
from timer import *
import argparse
config = json.load(open(os.path.dirname(os.path.realpath(__file__))+"/config"))

def work(work_time, timeStamp):
    os.system('setterm -cursor off')   
    child = playWorkSong()
    print "====================WORK WOKR====================\n"    
    while int(time.time()) < int(work_time*60) + int(timeStamp):
        #sys.stdout.write("==================\r")
        #sys.stdout.write("\r")         
        sys.stdout.write("THE FINAL COUNTDOWN : %s\r" % sec2time(int(work_time*60) - int(time.time()) + int(timeStamp)))        
        #sys.stdout.write("==================\r")        
        sys.stdout.flush()
    sys.stdout.write("THE FINAL COUNTDOWN : %s\r" % sec2time(int(work_time*60) - int(time.time()) + int(timeStamp)))                
    os.system('setterm -cursor on')     
    print      
    print  
    child.terminate()
def rest(rest_time, timeStamp, title, artist, url):
    os.system('setterm -cursor off')     
    child = playFMsong(url)
    print "====================REST REST====================\n"    
    print "CURRENT PLAYING : %s\n" % title + "--" + artist  
    while int(time.time()) < int(rest_time*60) + int(timeStamp):      
        sys.stdout.write("THE LAST COUNTDOWN : %s\r" % sec2time(int(rest_time*60) - int(time.time()) + int(timeStamp)))              
        sys.stdout.flush()
    sys.stdout.write("THE LAST COUNTDOWN : %s\r" % sec2time(int(rest_time*60) - int(time.time()) + int(timeStamp)))                
    os.system('setterm -cursor on')     
    print 
    print  
    child.terminate()
def rest_play_local(rest_time, timeStamp, playList):
    os.system('setterm -cursor off')     
    (child, songName) = playRandomSong(playList)
    print "====================REST REST====================\n"    
    print "CURRENT PLAYING : %s\n" % songName  
    while int(time.time()) < int(rest_time*60) + int(timeStamp):      
        sys.stdout.write("THE LAST COUNTDOWN : %s\r" % sec2time(int(rest_time*60) - int(time.time()) + int(timeStamp)))              
        sys.stdout.flush()
    sys.stdout.write("THE LAST COUNTDOWN : %s\r" % sec2time(int(rest_time*60) - int(time.time()) + int(timeStamp)))                
    os.system('setterm -cursor on')     
    print 
    print  
    child.terminate()        
    
if __name__ == '__main__':
    #parse the arguments, "local" to play local music, "douban" to play douban FM
    parser = argparse.ArgumentParser()
    parser.add_argument("method", nargs='?', default="local")
    args = parser.parse_args()
    if args.method == "douban":
        #print "using douban FM"
        (user_id, expire, token, user_name) = login(config['username'], config['password'])
        print "Hello " + user_name + "!"    
        channel  = config['channel']
        songlist = {}
        songlist['song'] = []
        try :    
            while True:
                if len(songlist['song']) < 1:
                    songlist = getSong(user_id, expire, token, channel)

                timeStamp = time.time()
                work(config["work_time"], timeStamp)

                artist = songlist['song'][len(songlist['song'])-1]['artist']
                title = songlist['song'][len(songlist['song'])-1]['title']
                url = songlist['song'][len(songlist['song'])-1]['url']  
                songlist['song'].pop()
                
                timeStamp = time.time()
                rest(config["rest_time"], timeStamp, title, artist, url)
        except KeyboardInterrupt:
            os.system('setterm -cursor on')  
            print "\n bye"            


    elif args.method == "local":
        print "using local music"
        try :    
            while True:
                timeStamp = time.time()
                work(config["work_time"], timeStamp)

                playList = getPlayList(config['music_dir'])
                timeStamp = time.time()
                rest_play_local(config["rest_time"], timeStamp, playList)
        except KeyboardInterrupt:
            os.system('setterm -cursor on')  
            print "\n bye"            

    else:
        print "wrong input, if you want to use douban FM, simply type : python pomoFM.py douban"

