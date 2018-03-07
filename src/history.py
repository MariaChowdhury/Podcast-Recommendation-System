#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 13:49:48 2018

@author: mariachowdhury

This script returns the watched episode by all users
"""
def user_history(user_history_file,user_episodes_file):
    import os
    import json
# =============================================================================
# user_history_file=os.getcwd()+"/private/"+"history.json"
# user_episodes_file=os.getcwd()+"/private/"+"user_episodes.txt"
# =============================================================================

    json_file=open(user_history_file,"r")
    strings = json.load(json_file)
    json_file.close()

    
    """collecting list of users and watched episodes in the .json files"""
    user_episodes=[]
    for key,val in strings.items():
        for k,v in val.items():
            user_key=key+","+k
            user_episodes.append(user_key)
                
        
    """writing output file that inclueds all users and watched episodes"""
        
    if os.path.exists(user_episodes_file):
        os.remove(user_episodes_file)
    
    user_episodes_write=open(user_episodes_file,"w")
    for v in user_episodes:
        user_episodes_write.write(v+ "\n")
   
        
    
# =============================================================================
user_history_file="/Users/mariachowdhury/Documents/Podcast-Recommendation-System/private/user_history.json"
user_episodes_file="/Users/mariachowdhury/Documents/Podcast-Recommendation-System/private/user_episodes.txt"
# 
# =============================================================================
user_history(user_history_file,user_episodes_file)