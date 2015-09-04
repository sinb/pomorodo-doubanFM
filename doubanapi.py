# -*- coding: utf-8 -*-
import requests
import urllib
import json
import subprocess
def login(username, password):
    login_data = {
                    'app_name': 'radio_desktop_win',
                    'version': '100',
                    'email': username,
                    'password': password
                 }    

    user_data = requests.post('http://www.douban.com/j/app/login',login_data) 
    udata = json.loads(user_data.text)   
    user_name = udata['user_name']        
    user_id = udata['user_id']
    expire = udata['expire']
    token = udata['token']
    return (user_id, expire, token, user_name)
    
def getSong(user_id, expire, token, channel):
    song_list = {
                    'app_name': 'radio_desktop_win',
                    'version': '100',
                    'user_id' : user_id,
                    'expire' : expire,
                    'token': token,
                    'type' : 'n',
                    'channel' : channel,
                }
    url = 'http://www.douban.com/j/app/radio/people?' + urllib.urlencode(song_list)
    song = requests.get(url)
    songlist = json.loads(song.text)
    return songlist    
def playFMsong(url):
    child = subprocess.Popen(['mpg123', '-q', url])
    return child    