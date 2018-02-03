#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 00:20:08 2018

@author: mariachowdhury
""checking if a string is substring of another string"""

def checkMatch(word,str,key):
    words=str.split(" ")
    for w in words:
        if w==word:
            return key
 

checkMatch('word','This word is example','http_')

