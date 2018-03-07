#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 14:10:08 2018

@author: mariachowdhury
"""

# =============================================================================
user=" "
watching="xyz"
user_social_recommendation_file="/Users/mariachowdhury/Documents/Podcast-Recommendation-System/private/user_social_recommendation.txt"
word_keys_file="/Users/mariachowdhury/Documents/Podcast-Recommendation-System/private/words_keys.txt"
# 
# =============================================================================

def generate_social_reco(user_social_recommendation_file):
    social_reco=[]
    with open(user_social_recommendation_file, mode="r",encoding="utf-8") as my_file:
        for line in my_file:
            social_reco.append(line.strip())
            return social_reco

def generate_semantic_reco(word_keys_file):
    semantic_reco=[]
    with open(word_keys_file, mode="r",encoding="utf-8") as my_file:
        for line in my_file:
            semantic_reco.append(line.strip())
            return semantic_reco

def generate_recommendation(user,watching,user_social_recommendation_file,word_keys_file):
    watching_words=watching.split(" ")
    reco=set()
    social_reco= generate_social_reco(user_social_recommendation_file)
    for line in social_reco:
        user_reco=line.split(",")
        if user_reco[0]==user:
            reco.add(user_reco[1])
    
    semantic_reco=generate_semantic_reco(word_keys_file)
    for word in watching_words:
        for line in semantic_reco:
            word_key=line.split(",")
            if word==word_key[0]:
                reco.add(word_key[1])
    return reco

 
def print_recommendation(user,watching,user_social_recommendation_file,word_keys_file):
    recommendation=[]
    recommendation= generate_recommendation(user,watching,user_social_recommendation_file,word_keys_file)
    if len(recommendation)>0:
        print(recommendation)

print_recommendation(user,watching,user_social_recommendation_file,word_keys_file)
