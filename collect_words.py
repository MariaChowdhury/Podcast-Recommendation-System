# -*- coding: utf-8 -*-
"""
Spyder Editor

This script creates the collection of available words in the input files
"""
import os
""" Location of json file and output file """

episode_data_file=os.getcwd()+"/"+"episode_data.json"
words_file=os.getcwd()+"/"+"words.txt"

"""reading from .json files"""
import json
json_file=open(episode_data_file,"r")
strings = json.load(json_file)
json_file.close()

    
"""collecting list of words in the .json files"""
val_words=[]
for key,val in strings.items():
    val_words.append(val["name"].split(" "))
    
  

"""adding all the words in a list"""
words=[]
for w in val_words:
        words=words+w
    
stop_words=['-','0','1','2','3','4','5','6','7','8','as','None','a','b','c','d','e','f','g','h','t','t','/','=','with','"there\'s','a','-','could','name',"let's",
            'i','j','k','l','m','n','o','p','to','us','what','and','but','let','hey','this','are','why','up','yet',
            'q','r','s','t','u','v','w','x','y','z','by','of','i','on','how','in','it','yes','not','we','the','does','is',
            'should','if','so','my',"you'll",'has',"can't",'get','he','pi','very','ai','rm','le',
            'can','could','you','there','about','were','me','where','why','003:','001:',
            '000:','002:','004:','005:','006:',"it's","there","there\'s'",'into','&',"ain't"
            ,'for','from','or','+','at','be','your','an','vs','via','all','did'
            ,"w/","_"]

stop_words.sort()

"""replacing (,),.,?"""
def replaceChar(word):
    word=word.replace(")","")
    word=word.replace("(","")
    word=word.replace("?","")
    word=word.replace(".","")
    word=word.replace(":","")
    word=word.replace("%","")
    word=word.replace("#","")
    word=word.replace(",","")
    word=word.replace("!","")
    word=word.replace("\"","")
    word=word.replace("|","")
    word=word.replace(" ","")
    word=word.replace("\'s","")
    return word
        


"""adding to set of words as a dictionary"""
word_set=set()  
for word in words:
        if replaceChar(word.lower()) not in stop_words:
            word_set.add(replaceChar(word.lower()))


   
"""writing to output words file"""
if os.path.exists(words_file):
    os.remove(words_file)
words_file=open(words_file,"w");
for word in word_set:
    replaceChar(word)
    words_file.write(word+ "\n")

print(len(word_set))



