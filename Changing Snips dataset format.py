# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 12:10:23 2020

@author: mohiu
"""



def clean_text(text):
    text = str(text)
    text = text.replace(':O','')
    text = text.replace(':B-',' ')
    text = text.replace(':I-',' ')
    
    text = text.split("<=>", 1)
    text = text[0]
    
    text= re.sub(' +', ' ',text)
    
    text = list(text.split(" "))
    char_list = ['_', '.'] 
    text = [ele for ele in text if all(ch not in ele for ch in char_list)] 
    text = ' '.join(text)
    text = "BOS " + text + "EOS"
    return text



sentence = []
intentAndSlot = []
import re
with open('testSmall.txt') as f:
  for line in f.readlines():       
    # 1. put your slots and intent code here and insert them in intentAndSlot list
      
        line = clean_text(line)
        sentence.append(line)
        print(line)
# 2. attach each row from sentence list to the corresponding row in intentAndSlot list in a loop
        
