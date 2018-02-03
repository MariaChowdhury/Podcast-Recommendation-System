# -*- coding: utf-8 -*-
"""
Spyder Editor
This script retrieves the episode url corresponding a keyword
"""
from checkWordValMatch import checkMatch

import os           
word_episode_file=os.getcwd()+"/"+"words_keys.txt"
if os.path.exists(word_episode_file):
    os.remove(word_episode_file)

"""loading dictionary """

dictionary_file=os.getcwd()+"/words.txt"
words=[]
with open(dictionary_file, mode="r",encoding="utf-8") as my_file:
    for line in my_file:
            words.append(line.strip())
            
#words.sort()    
"""reading data from .json files"""
import json
data_file=os.getcwd()+"/"+"episode_data.json"
json_file=open(data_file,"r")
strings = json.load(json_file)
json_file.close()


"""populating a hashmap with word as a key and episode url as values"""
words_file=open(word_episode_file,"w");
word_episode={}
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
            
            
        
        



    
           

#print(words)         
