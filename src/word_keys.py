# -*- coding: utf-8 -*-
"""
Spyder Editor
This script retrieves the episode url corresponding a keyword
"""
def word_keys(word_episode_file,dictionary_file):
    import os           
    if os.path.exists(word_episode_file):
        os.remove(word_episode_file)

    """loading dictionary """
    
    words=[]
    with open(dictionary_file, mode="r",encoding="utf-8") as my_file:
        for line in my_file:
                words.append(line.strip())
            
    
    """reading data from .json files"""
    import json
    data_file="/Users/mariachowdhury/Documents/Podcast-Recommendation-System/private/"+"episode_data.json"
    json_file=open(data_file,"r")
    strings = json.load(json_file)
    json_file.close()


    """checking if a string is substring of another string"""
    
    def checkMatch(word,str,key):
        words=str.split(" ")
        for w in words:
            if w==word:
                return key


    """populating a hashmap with word as a key and episode url as values"""
    words_file=open(word_episode_file,"w");
    for word in words:
        for key,val in strings.items():
            str=val["name"]
            match=checkMatch(word,str,key)
            if match:
                if word:
                    str1=word+','+key
                    words_file.write(str1+"\n")
            else:
                continue
            
            
word_episode_file="/Users/mariachowdhury/Documents/Podcast-Recommendation-System/private/words_keys.txt"
dictionary_file="/Users/mariachowdhury/Documents/Podcast-Recommendation-System/private/words.txt"
                
word_keys(word_episode_file,dictionary_file)
