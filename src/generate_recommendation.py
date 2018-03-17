#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 14:10:08 2018

@author: mariachowdhury
"""

def generate_recommendation(user,watching_episode,user_social_recommendation_file,word_keys_file):
    """list of recommenadtion generated"""
    recommendation=[]
    
    """higher rank recommendation from social network"""
    top_recommendation=set()
    
    """recommendation from currently watching episode"""
    name_recommendation=set()
    
    """list of all episodes"""
    all_episode=[]
    
    """recommendation collected from user"""
    social_recommendation=[]
    
    with open(user_social_recommendation_file, mode="r",encoding="utf-8") as my_file:
            for line in my_file:
                social_recommendation.append(line.strip())
                
    with open(word_keys_file, mode="r",encoding="utf-8") as my_file:
            for line in my_file:
                all_episode.append(line.strip())
                
    """removing stopwords and stemming the words of watching_episode"""
    my_stop_words=['in','-','be','how','so','that','can','will','vs','en','other'
                   ,'have','via','do','the','did','about','what']
    words=set()
    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer
    ps=PorterStemmer()
    watching_episode=watching_episode.split();
    for i in range(0,len(watching_episode)):
      name=watching_episode[i].split()
      name=[ps.stem(word) for word in name if not word in set(stopwords.words('english'))]
      for word in name:
          if word not in my_stop_words:
              words.add(word.lower())
    #print(words)
    
    
    """collecting recommendation from social recommendation and 
    from current watching episode"""
    
    for line in social_recommendation:
       user_reco=line.split(",")
       if user_reco[0]==user:
           top_recommendation.add(user_reco[1])
    
    for word in words:
        for alt_reco in all_episode:
            alt_reco=alt_reco.split(",")
            if alt_reco[0]==word:
                name_recommendation.add(alt_reco[1])
    
     
    for reco in top_recommendation:
        recommendation.append(reco)
    for reco in name_recommendation:
        if reco not in top_recommendation:
            recommendation.append(reco)
      
    print(recommendation)
# =============================================================================
user="ehSOn58nzLZlSjoefzm7914iEFn2"
watching_episode="What Did You Like Least About Your Last Job?"
user_social_recommendation_file="/Users/mariachowdhury/Documents/Podcast-Recommendation-System/private/user_social_recommendation.txt"
word_keys_file="/Users/mariachowdhury/Documents/Podcast-Recommendation-System/private/words_keys.txt"
# =============================================================================
generate_recommendation(user,watching_episode,user_social_recommendation_file,word_keys_file)


    


