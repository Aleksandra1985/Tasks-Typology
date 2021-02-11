#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter.filedialog import *
from tkinter.messagebox import *
import chardet
from gensim import corpora, models
#from settings import stopwords
import codecs
import sys, os
import os.path
import nltk
import re
import requests
import numpy
from numpy import *
import nltk
import scipy
from tkinter import Tk
from tkinter.filedialog import *
from tkinter.messagebox import *
from settings import stem
from nltk.corpus import stopwords
from nltk.stem import  SnowballStemmer
import re
stemmer = SnowballStemmer(stem)
import matplotlib.pyplot as plt
import matplotlib as mpl

 TASK EXECUTION ASPECTS:

# Step 4.1. Typology Aspect Extraction (Tasks)

# MAIN STAGES:
# STAGE 1. Tasks Corpus Reading
# STAGE 2. Find the words in the Task that match the Task Typology Vocabulary Keywords
# STAGE 3. Defining Task Type of each Task
# STAGE 4. Writing the results in the *.csv file

def word_count(stopword):
    
   k_b=0
   path='C:/Users/Tasks/Texts'
   k=0
   
   fb1=open('C:/Users/Tasks_Types_3.doc', 'wb')
   a=sorted(os.listdir(path))
   

# _________________STAGE 1. Tasks Corpus Reading_________________________________________________________
   #print(Fa_stem)
   for i in a[0:124733]:
   #for i in a[0:5]:
      print('# Doc'+str(i))
      kkk="-"
      kkk1="-"
      kkk2="-"
      kkk3="-"
      e=[]
      enc=0
      filename1=str(i)
      filename=path+'/'+str(i)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:

         for line in file_object:
            line = line.rstrip('\n')
            a = line.strip()
  
            #Tasks

 # STAGE 2.1. Find and Count the number of words in the Task that match the PSO task Vocabulary Keywords
            text2 = re.findall(r'offline', a)
            text3 = re.findall(r'index', a)
            text4 = re.findall(r'mode', a)
            text5 = re.findall(r'downtime', a)
            text6 = re.findall(r'page', a)
            text7 = re.findall(r'tool', a)
            text8 = re.findall(r'Stop Anwendung', a)
            text9 = re.findall(r'session', a)
            text10 = re.findall(r'pso', a)
            text11 = re.findall(r'outage', a)
            text12 = re.findall(r'shutdown', a)
                        
            if text2!=[] or text3!=[] or text4!=[] or text5!=[] or text6!=[] or text7!=[] or text8!=[] or text9!=[] or text10!=[] or text11!=[] or text12!=[] or text13!=[]:
               kkk="PSO"
            else:
               kkk="-"
# STAGE 2.2. Find and Count the number of words in the Task that match the QA task Vocabulary Keywords

            text18 = re.findall(r'Health check', a)
            text19 = re.findall(r'check', a)
            text20 = re.findall(r'Health', a)
            text21 = re.findall(r'health check', a)
            text22 = re.findall(r'verify', a)
            text23 = re.findall(r'software monitoring', a)
            text24 = re.findall(r'test', a)
            text25 = re.findall(r'reboot', a)
            text26 = re.findall(r'Kontrolle', a)
            text27 = re.findall(r'pre-check', a)
            text271 = re.findall(r'4 EP', a)
            text272 = re.findall(r'4EP', a)
            text273 = re.findall(r'Four eyes principle', a)
            text274 = re.findall(r'QS', a)
            text275 = re.findall(r'QA', a)
            
            
# STAGE 2.2. Find and Count the number of words in the Task that match the Implementation task Vocabulary Keywords

            text28 = re.findall(r'application', a)
            text29 = re.findall(r'team', a)
            text30 = re.findall(r'server', a)
            text31 = re.findall(r'production', a)
            text32 = re.findall(r'environment', a)
            text33 = re.findall(r'user', a)
            text34 = re.findall(r'requirements', a)
            text35 = re.findall(r'service', a)
            text351 = re.findall(r'script', a)
            text352 = re.findall(r'database', a)
            text353 = re.findall(r'delete', a)
    
            

# STAGE 3. Defining Task Type of each Task                          
            if text2!=[] or text3!=[] or text4!=[] or text5!=[] or text6!=[] or text7!=[] or text8!=[] or text9!=[] or text10!=[] or text11!=[] or text12!=[] or text13!=[]:
               kkk="PSO"
            else:
               kkk="-"
            if text18!=[] or text19!=[] or text20!=[] or text21!=[] or text22!=[] or text23!=[] or text24!=[] or text25!=[] or text26!=[] or text27!=[] or text271!=[] or text272!=[] or text273!=[]or text274!=[] or text275!=[]:
               kkk1="QA"
            else:
               kkk1="-"

            if text28!=[] or text29!=[] or text30!=[] or text31!=[] or text32!=[] or text33!=[] or text34!=[] or text35!=[] or text351!=[]or text352!=[] or text353!=[]:
               kkk2="Implementation"
            else:
               kkk2="-"

            if kkk=="-" and  kkk1=="-" and kkk3=="-":
               kkk2="Implementation"
               
            print(str(kkk), str(kkk1), str(kkk3))
            
# _____________________STAGE 4. Writing the results in the *.csv file___________________________________

            fb1.write(bytes('"File"."PSO"."Implementation"."Quality Assurance"'+'\n', 'UTF-8'))   
            fb1.write(bytes(str(filename1)+'. '+str(kkk)+'. '+str(kkk1)+'. '+str(kkk2)+'. '+str(kkk3), 'UTF-8'))          
             fb1.write(bytes('\n', 'UTF-8'))
  
   fb1.close()
   
stopwords1=['the', 'a', 'in ', 'for', 'to', 'of', 'and', 'ABC', 'of', 'on', 'at', 
         'or', 'if', 'end', 'were','each', 'was', 'as','has', 'how', 'it', 
           'may', 'often', 'be',  'done', 'these', 'all', 'etc', 'made',
          'make', ' the', 'about', 'also', 'always', 'as', 'can',
           'but', 'do', 'get', 'go', 'how', 'is', 'it',  'just', 'lot', 'able',
           'off', 'them', 'they', 'this', 'thus',  'up', 'us', 'very',
           'why', 'your', 'need', ' must', 'now', 'so', 'some',
           'became', 'still', 'stay', 'take', 'took', 'want', 'say',
           'while', 'who', 'you', 'thank', 'new', 'psi', 'busy', 'any',
           'only','a','about','above','after','again','against','all','am','an',
           'and','any','are','aren’t','as','at','be','because','been','before',
           'being','below','between','both','but','by','can’t','cannot','could',
           'couldn’t','did','didn’t','do','does','doesn’t','doing','don’t','down','during',
           'each','few','for','from','further','had','hadn’t','has','hasn’t','have','haven’t',
           'having','he','he’d','he’ll','he’s','her','here','here’s','hers','herself','him','himself',
           'his','how','how’s','i','I’d','I’ll','I’m','I’ve','if','in','into','is','isn’t','it','it’s','its','itself',
           'let’s','me','more','most','mustn’t','my','myself','no','nor','not','of','off','on','once',
           'only','or','other','ought','our','ours','ourselves','out','over','own','same','shan’t',
           'she','she’d','she’ll','she’s','should','shouldn’t','so','some','such','than','that','that’s',
           'the','their','theirs','them','themselves','then','there','there’s','these','they','they’d',
           'they’ll','they’re','they’ve','this','those','through','to','too','under','until','up','very',
           'was','wasn’t','we','we’d','we’ll','we’re','we’ve','were','weren’t','what','what’s','when',
           'when’s','where','where’s','which','while','who','who’s','whom','why','why’s','with','won’t',
           'would','wouldn’t','you','you’d','you’ll','you’re','you’ve','your','yours','yourself','yourselves'
           'get', 'our', 'out', 'set', 'such', 'take', 'have', 'did',
           'than', 'their', 'then', 'well', 'in', 'when', 'his', 'even',
           'what', 'due', 'via', 'from', 'do', 'does', 'thus', 'sit',
           'he', 'an', 'over', 'had', 'would', 'whoever', 'after',
           'with', 'which', 'within', 'where', 'come', 'more',
           'there', 'their', 'be', 'between', 'been',  'through',
           'can', 'is', 'this', 'we', 'will', 'give', 'without', 'by',  'itself', 'http'
           'about', 'does', 'not', 'that', 'no', 'but', 'are', 'keep','mr', 'ms', 'ayakkab', 'allah', 'bunyamin', '\ufeff']
stem='english'



word_count(stopwords)
 
