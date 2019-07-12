#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 17:40:38 2019

@author: lillian
"""

def language_frequency(file_name): # creates function to calculate frequency and check unknown languages against languages
    with open(file_name) as file_object:
        contents = file_object.read()
    
    s = contents.split()
    List = []
    for word in s:
        x = word.lower().strip('&%$#@!^ _+=`:;"><?/\.¡,¿ --¿')
        List.append(x)
    

#print(len(List))#returns 44468
    counts = {}# creates a dict of the words in the text file 
    for word in List:
        if not word in counts:
            counts[word] = 0
            counts[word] += 1
       
            for word in counts.keys():
                counts[word] = counts[word]/len(List)
    sorted_counts = sorted(counts.items(), key=lambda kv: kv[1]) #sorts dict by frequency with largetst count at end of dict.
    most_frequent = sorted_counts[-10:]#returns the 10 most frequent 
    return most_frequent

en = (language_frequency('eaton-boy-scouts_EN.txt'))# these variables stand iin for each file 
sp = (language_frequency('cherbonnel-mi-tio_SP.txt'))
de = (language_frequency('schloemp-tolle-koffer_DE.txt'))
uk = (language_frequency('unknown-lang.txt'))

Sb=0
Eb=0
Db=0

for w in uk.keys():# If there is a corresponding value to the given key, it will be returned. 
   U = uk.get(w, 0)#This is applied to each language file
   E = en.get(w, 0)
   Ediff=abs(E-U)#The difference between the frequencies of words in each language file and the unknown file. This is performed for each language and returned as an absolute value.
   Eb = Eb + Ediff# This variable returns thes sum of the absolute difference as a variable
   
   D = de.get(w, 0)
   Ddiff=abs(D-U)
   Db = Db + Ddiff
  
   S = sp.get(w, 0)
   Sdiff=abs(S-U)
   Sb= Sb + Sdiff

if Sb < Eb and Sb < Db:
    print('Spanish!')## prints Spanish for this particular instance
elif Eb < Sb and Eb < Db:
    print ('English!')
elif Db < Sb and Db < Eb:
    print ('German')