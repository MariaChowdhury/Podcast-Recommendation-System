#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 10:25:29 2018

@author: mariachowdhury
"""

"""function to collect episodes watched by a user"""
def get_episode_list(fr,episodes):
    episode_list=[]
    for episode in episodes:
        episode_str=episode.split(",")
        if episode_str[0]==fr:
            episode_list.append(episode_str[1])
            return episode_list
            
def user_social_recommendation(user_file,user_history_file,user_social_recommendation_file):
    import json
    """loading user history """
    episodes=[]
    with open(user_history_file, mode="r",encoding="utf-8") as my_file:
        for line in my_file:
                episodes.append(line.strip())

            
    """loading users and their friends"""            
    json_file=open(user_file,"r")
    strings = json.load(json_file)
    json_file.close()
             
            
    """generating recommendation based on social network"""
    import os
    if os.path.exists(user_social_recommendation_file):
        os.remove(user_social_recommendation_file)
        
    social_recommendation_write=open(user_social_recommendation_file,"w")
    
    for key,val in strings.items():
        episode_list=[]
        if val.get("friends")!=None:
            friends=val.get("friends")
            for fr in friends:
                episode_list=get_episode_list(fr,episodes)
                if episode_list!=None:
                    for epi in episode_list:
                        epi_key=key+","+epi
                        social_recommendation_write.write(epi_key+"\n")
    
# =============================================================================
user_file="/Users/mariachowdhury/Documents/Podcast-Recommendation-System/private/social_network.json"
user_watched_file="/Users/mariachowdhury/Documents/Podcast-Recommendation-System/private/user_episodes.txt"
user_social_recommendation_file="/Users/mariachowdhury/Documents/Podcast-Recommendation-System/private/user_social_recommendation.txt"
# 
# =============================================================================
user_social_recommendation(user_file,user_watched_file,user_social_recommendation_file)

            
    
                    

              

    
   