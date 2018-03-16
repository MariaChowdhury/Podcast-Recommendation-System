# -*- coding: utf-8 -*-
"""
Spyder Editor

This script creates the collection of available words in the input files
"""

def collect_words(episode_data_file,words_file):
    """loading data from file"""
    import pandas as pd
    import numpy as np
    dataset=pd.read_json(episode_data_file)
    transposed_dataset=np.transpose(dataset)
    name=transposed_dataset['name']

    """removing unnecessary words"""
    valid_name=[]
    import re
    for i in range(0,len(name)):
        valid_name.append(re.sub('[^a-zA-Z]'," ",name[i].lower()))
    

    """removing stopwords and stemming the words"""
    words=set()
    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer
    ps=PorterStemmer()
    for i in range(0,len(valid_name)):
        name=valid_name[i].split()
        name=[ps.stem(word) for word in name if not word in set(stopwords.words('english'))]
        for word in name:
            words.add(word)

    """writing to output words file"""
    import os
    if os.path.exists(words_file):
       os.remove(words_file)
    words_file=open(words_file,"w");
    for word in words:
        words_file.write(word+ "\n")

# =============================================================================
# episode_data_file="/Users/mariachowdhury/Documents/Podcast-Recommendation-System/private/episode_data.json"
# words_file="/Users/mariachowdhury/Documents/Podcast-Recommendation-System/private/words.txt"
# collect_words(episode_data_file,words_file)
# 
# =============================================================================
