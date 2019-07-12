# LanguageDetectorProgram-IMT511
This program detects which language was used to draft a text file.

## Languages detected

* English
 
* German

* Spanish
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 17:40:38 2019

@author: lillian
"""

def language_frequency(file_name):
    with open(file_name) as file_object:
        contents = file_object.read()
    #print(contents)#prints file
    s = contents.split()
    List = []
    for word in s:
        x = word.lower().strip('&%$#@!^ _+=`:;"><?/\.¡,¿ --¿')
        List.append(x)
    

#print(len(List))#returns 44468
    counts = {}
    for word in List:
        if not word in counts:
            counts[word] = 0
            counts[word] += 1
       
            for word in counts.keys():
                counts[word] = counts[word]/len(List)
    sorted_counts = sorted(counts.items(), key=lambda kv: kv[1])
    most_frequent = sorted_counts[-10:]
    return most_frequent
#sorted_dict = dict(sorted_counts)
#print(sorted_dict)
#most_frequent = sorted_dict[:11]
print(language_frequency('cherbonnel-mi-tio_SP.txt'))