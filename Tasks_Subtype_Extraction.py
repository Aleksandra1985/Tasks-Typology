#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter.filedialog import *
from tkinter.messagebox import *
import numpy as np
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

stemmer = SnowballStemmer(stem)
import matplotlib.pyplot as plt
import matplotlib as mpl

# Step 4.2. Typology Aspect Extraction (SubTasks)

# MAIN STAGES:

# STAGE 1. SubTask Typology Vocabulary (1.1.) Reading and (1.2) Stemming
# STAGE 2. Tasks Type Corpus (2.1.) Reading, Special Preprocessing and (2.2.) English language filtering
# STAGE 3. Find and Count the number of words in the Task that match the SubTask Typology Vocabulary Keywords
# STAGE 4. Writing of Matched words and their Number in the *.csv file
#________________________________________________________________________________


def word_count(stopword):

# STAGE 2.1. SubTaskTask Typology Vocabulary Reading_____________________________

#___________________PSO Subtasks_________________________________________________


   path='C:/Users/Task_Types'

   #_______Planning________
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'Planning.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s1=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            line=line.lower()
            #print(line)
            s1.append(line)
   #print(s1)
   

   #_______Execution________
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'Execution.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s2=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            line=line.lower()
            #print(line)
            s2.append(line)
   #print(s2)

   #_______Check________
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'Check.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s3=[]
         
                   
         for line in file_object:
            line = line.rstrip('\n\r')
            line=line.lower()
            #print(line)
            s3.append(line)

#________________Implementation Subtasks________________________________________
            
   #_______Preparation items________
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'Preparation.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s4=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            line=line.lower()
            #print(line)
            s4.append(line)
   #print(s4)

   #_______Configuration________
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'Configuratione.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s5=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            line=line.lower()
            #print(line)
            s5.append(line)
   #print(s5)

   #_______Installation________
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'Installation.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s6=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            line=line.lower()
            #print(line)
            s6.append(line)
   #print(s6)

   #_______Update________
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'Update.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s7=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            line=line.lower()
            #print(line)
            s7.append(line)
   #print(s7)

   #_______Upgrade________
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'Upgrade.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s8=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            line=line.lower()
            #print(line)
            s8.append(line)
   #print(s8)

   #_______Capacity________
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'Capacity.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s9=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            line=line.lower()
            #print(line)
            s9.append(line)
   #print("s9=",s9)

   #_______integration________
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'Reset configuration.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s10=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            line=line.lower()
            #print(line)
            s10.append(line)
   #print(s10)

   #_______Incident/ problem________
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'Incident/ problem.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s11=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            line=line.lower()
            #print(line)
            s11.append(line)
   #print(s11)
   
   
   #_______Release________
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'Release.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s12=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            line=line.lower()
            #print(line)
            s12.append(line)
   #print(s1)

   #_______Service delivery________
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'Service delivery.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s13=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            line=line.lower()
            #print(line)
            s13.append(line)
   #print(s1)

   #_______Support________
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'Support.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s14=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            line=line.lower()
            #print(line)
            s14.append(line)
   #print(s1)

   #_______Migration________
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'Migration.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s15=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            line=line.lower()
            #print(line)
            s15.append(line)
   #print(s1)

   #_______Decommission________
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'Decommission.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s16=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            line=line.lower()
            #print(line)
            s16.append(line)
   #print(s1)
#___________________Quality Assurance Subtasks_________________________________________________


   path='C:/Users/Quality_Assurance_Types'

   #_______4EP________
   a17=sorted(os.listdir(path))
   for i in a17[0:1]:
      filename=path+'/'+'4EP.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s17=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            line=line.lower()
            #print(line)
            s17.append(line)
   #print(s1)
   

   #_______Backup & health check________
   a18=sorted(os.listdir(path))
   for i in a18[0:1]:
      filename=path+'/'+'Backup_health_check.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s18=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            line=line.lower()
            #print(line)
            s18.append(line)
 
   #_______Software monitoring________
   a19=sorted(os.listdir(path))
   for i in a19[0:1]:
      filename=path+'/'+'Software_monitoring.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s19=[]
         
                   
         for line in file_object:
            line = line.rstrip('\n\r')
            line=line.lower()
            #print(line)
            s19.append(line)

#_______Update test________
   a20=sorted(os.listdir(path))
   for i in a20[0:1]:
      filename=path+'/'+'Update_test.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s20=[]
         
                   
         for line in file_object:
            line = line.rstrip('\n\r')
            line=line.lower()
            #print(line)
            s20.append(line)
#_________________________________________________________
            
# STAGE 2.1. PSO Tasks SubCorpus Reading, Preprocessing       
#_________________________________________________________ 

   k_b=0
   path='C:/Users/PSO_ Tasks_Texts'
   k=0
   fb=open('C:/Users/PSO_Statistics_3.doc', 'wb')
   a=sorted(os.listdir(path))
   
   #k_w=0
   #k_o=0   
   for i in a[0:N]:
      print('# '+str(i))
      e=[]
      enc=0
      
      filename=path+'/'+str(i)


      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         #fb.write(bytes(str(i)+'; ', 'UTF-8')) 
         for line in file_object:
            line = line.rstrip('\n')
            a = line.strip()
            #print(a)
            
            if len(a)==0:
               enc=enc+1
  
            if enc==0:
            
               if len(line.strip())!=0:
                  
                  k=k+1
                  text=line.strip()
                  text=text.lower()
                  #print (text)
                  
                  text1=[]
                  text2=[]
                  text3=[]
                  text4=[]
                                    
                  filename1=str(i)
                  fb.write(bytes(str(filename1)+'; ', 'UTF-8'))
                  
                  #print(m)
                  da={}
                  ds={}
                  dv={}
                  d={}
                  b=[]
                  oo1=[]
                  oo2=[]
                  oo3=[]
                  yy=[]

# STAGE 3.1 Find and Count the number of words in the Task that match the PSO SubTasks Typology Vocabulary Keywords
#___________________PSO Subtasks__________________________________________________________________________________                  

                #_______planning________
                     ff1=len(s1)
 
                     ddd1=len(s1)-1
                     hh=np.arange(0, ddd1, 1)
                     for i in hh[0:ddd1]:
                        text1 = re.findall(s1[i], text)
                        if text1!=[]:
                           oo1.append(text1)
                                                             
                     a1=len(oo1)
 
                  except:
                     pass

                  #_______execution________
                  try:
                     ff2=len(s2)
  
                     ddd2=len(s2)-1
                     hh=np.arange(0, ddd2, 1)
                     for i in hh[0:ddd2]:
                        text2 = re.findall(s2[i], text)
                        #print(text2)
                        if text2!=[]:
                           oo2.append(text2)
                                                             
                     a2=len(oo2)
  
                  except:
                     pass

                  #_______check________
                  try:
                     ff3=len(s3)
  
                     ddd3=len(s3)-1
                     hh=np.arange(0, ddd3, 1)
                     for i in hh[0:ddd3]:
                        text3 = re.findall(s3[i], text)
                        if text3!=[]:
                           oo3.append(text3)
                                                             
                     a3=len(oo3)
  
                  except:
                     pass

#_________STAGE 4.1. Writing of Matched words and their Number in the *.csv file______________
           
                     fb.write(bytes('File; Planning; Words; Execution; Words; Check; Words;'+'\n', 'UTF-8'))
                     fb.write(bytes(str(oo1)+';'+str(a1)+';'+str(oo2)+';'+str(a2)+';'+str(oo3)+';'+str(a3), 'UTF-8'))
                  fb.write(bytes('\n', 'UTF-8'))
 
                     
   
   fb.close()
#_________________________________________________________
            
# STAGE 2.2. Implementation Tasks SubCorpus Reading, Preprocessing       
#_________________________________________________________ 

   k_b=0
   path='C:/Users/Implementation_ Tasks_Texts'
   k=0
   fb=open('C:/Users/Implementation_Statistics_3.doc', 'wb')
   a=sorted(os.listdir(path))
   
   #k_w=0
   #k_o=0   
   for i in a[0:NN]:
      print('# '+str(i))
      e=[]
      enc=0
      
      filename=path+'/'+str(i)


      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         #fb.write(bytes(str(i)+'; ', 'UTF-8')) 
         for line in file_object:
            line = line.rstrip('\n')
            a = line.strip()
            #print(a)
            
            if len(a)==0:
               enc=enc+1
  
            if enc==0:
            
               if len(line.strip())!=0:
                  
                  k=k+1
                  text=line.strip()
                  text=text.lower()
                  #print (text)
                  
                  
                  text4=[]
                  text5=[]
                  text6=[]
                  text7=[]
                  text8=[]
                  text9=[]
                  text10=[]
                  text11=[]
                  text12=[]
                  text13=[]
                  text14=[]
                  text15=[]
                  text16=[]
                  
                  filename1=str(i)
                  fb.write(bytes(str(filename1)+'; ', 'UTF-8'))
                  
                  #print(m)
                  da={}
                  ds={}
                  dv={}
                  d={}
                  b=[]
                  
                  oo4=[]
                  oo5=[]
                  oo6=[]
                  oo7=[]
                  oo8=[]
                  oo9=[]
                  oo10=[]
                  oo11=[]
                  oo12=[]
                  oo13=[]
                  oo14=[]
                  oo15=[]
                  oo16=[]
                  yy=[]

# STAGE 3.2. Find and Count the number of words in the Task that match the Implementation SubTasks Typology Vocabulary Keywords

#___________________Implementation Subtasks________________________________________________________________ 

                 #_______preparation________
                  try:
                     ff4=len(s4)
 
                     ddd4=len(s4)-1
                     hh=np.arange(0, ddd4, 1)
                     for i in hh[0:ddd4]:
                        text4 = re.findall(s4[i], text)
                        if text4!=[]:
                           oo4.append(text4)
                                                             
                     a4=len(oo4)
   
                  except:
                     pass

                  
                  #_______configuration________

                  try:
                     ff5=len(s5)
   
                     ddd5=len(s5)-1
                     hh=np.arange(0, ddd5, 1)
                     for i in hh[0:ddd5]:
                        text5 = re.findall(s5[i], text)
                        if text5!=[]:
                           oo5.append(text5)
                                                             
                     a5=len(oo5)
  
                  except:
                     pass

                  #_______installation________

                  try:
                     ff6=len(s6)
   
                     ddd6=len(s6)-1
                     hh=np.arange(0, ddd6, 1)
                     for i in hh[0:ddd6]:
                        text6 = re.findall(s6[i], text)
                        if text6!=[]:
                           oo6.append(text6)
                                                             
                     a6=len(oo6)
  
                  except:
                     pass

                  #_______update________

                  try:
                     ff7=len(s7)
  
                     ddd7=len(s7)-1
                     hh=np.arange(0, ddd7, 1)
                     for i in hh[0:ddd7]:
                        text7 = re.findall(s7[i], text)
                        if text7!=[]:
                           oo7.append(text7)
                                                             
                     a7=len(oo7)
  
                  except:
                     pass

                  #_______upgrade_______

                  try:
                     ff8=len(s8)
   
                     ddd8=len(s8)-1
                     hh=np.arange(0, ddd8, 1)
                     for i in hh[0:ddd8]:
                        text8 = re.findall(s8[i], text)
                        if text8!=[]:
                           oo8.append(text8)
                                                             
                     a8=len(oo8)
     
                  except:
                     pass

                  #_______capacity________

                  try:
                     ff9=len(s9)
   
                     
                     ddd9=len(s9)-1
   
                     hh=np.arange(0, ddd9, 1)
                     for i in hh[0:ddd9]:
                        #print('i=',i)
                        text9 = re.findall(s9[i], text)
                        if text9!=[]:
                           oo9.append(text9)
                                                             
                     a9=len(oo9)
   
                  except:
                     pass

                  #_______integration________

                  try:
                     ff10=len(s10)
    
                     ddd10=len(s10)-1
                     hh=np.arange(0, ddd10, 1)
                     for i in hh[0:ddd10]:
                        text10 = re.findall(s10[i], text)
                        if text10!=[]:
                           oo10.append(text10)
                                                             
                     a10=len(oo10)
    
                  except:
                     pass

                  #_______incident/ problem________

                  try:
                     ff11=len(s11)
    
                     ddd11=len(s11)-1
                     hh=np.arange(0, ddd11, 1)
                     for i in hh[0:ddd11]:
                        text11 = re.findall(s11[i], text)
                        if text11!=[]:
                           oo11.append(text11)
                                                             
                     a11=len(oo11)
     
                  except:
                     pass

                  #_______release ____________
                  

                  try:
                     ff1=len(s12)
        
                     ddd1=len(s12)-1
                     hh=np.arange(0, ddd1, 1)
                     for i in hh[0:ddd1]:
                        text12 = re.findall(s12[i], text)
                        if text12!=[]:
                           oo12.append(text12)
                                                             
                     a12=len(oo12)
           
                  except:
                     pass
    

                  #_______service delivery________

                  try:
                     ff1=len(s13)
   
                     ddd1=len(s13)-1
                     hh=np.arange(0, ddd1, 1)
                     for i in hh[0:ddd1]:
                        text13 = re.findall(s13[i], text)
                        if text13!=[]:
                           oo13.append(text13)
                                                             
                     a13=len(oo13)
         
                  except:
                     pass
       
                  #_______support ________

                  try:
                     ff1=len(s14)
            
                     ddd1=len(s14)-1
                     hh=np.arange(0, ddd1, 1)
                     for i in hh[0:ddd1]:
                        text14 = re.findall(s14[i], text)
                        if text14!=[]:
                           oo14.append(text14)
                                                             
                     a14=len(oo14)
          
                  except:
                     pass
          
                  #_______migration________

                  try:
                     ff1=len(s15)
         
                     ddd1=len(s15)-1
                     hh=np.arange(0, ddd1, 1)
                     for i in hh[0:ddd1]:
                        text15 = re.findall(s15[i], text)
                        if text15!=[]:
                           oo15.append(text15)
                                                             
                     a15=len(oo15)
      
                  except:
                     pass
      

                  #_______decommission________

                  try:
                     ff1=len(s16)
   
                     ddd1=len(s16)-1
                     hh=np.arange(0, ddd1, 1)
                     for i in hh[0:ddd1]:
                        text16 = re.findall(s16[i], text)
                        if text16!=[]:
                           oo16.append(text16)
                                                             
                     a16=len(oo16)
     
                  except:
                     pass
    
                
#_________STAGE 4.2. Writing of Matched words in the *.csv file______________
           
                     fb.write(bytes('File; Preparation; Words; Configuration; Words; Installation; Words; Update; Words; Upgrade; Words; Capacity; Words; integration;Words; Incident/problem; Words;Release; Words; Service delivery; Words; Support; Words; Migration; Words;Decommission; Words'+'\n', 'UTF-8'))
                     fb.write(bytes(str(oo1)+';'+str(a1)+';'+str(oo2)+';'+str(a2)
                                 +';'+str(oo3)+';'+str(a3)+';'+str(oo4)+';'+str(a4)
                                 +';'+str(oo5)+';'+str(a5)+';'+str(oo6)+';'+str(a6)
                                 +';'+str(oo7)+';'+str(a7)+';'+str(oo8)+';'+str(a8)
                                 +';'+str(oo9)+';'+str(a9)
                                 +';'+str(oo10)+';'+str(a10)+';'+str(oo11)+';'+str(a11)
                                 +';'+str(oo12)+';'+str(a12)+';'+str(oo13)+';'+str(a13)
                                 +';'+str(oo14)+';'+str(a14)+';'+str(oo15)+';'+str(a15)
                                 +';'+str(oo16), 'UTF-8'))
                  fb.write(bytes('\n', 'UTF-8'))
 
                     
   
   fb.close()
# STAGE 2.3. QA Tasks SubCorpus Reading, Preprocessing       
#_________________________________________________________ 

   k_b=0
   path='C:/Users/QA_ Tasks_Texts'
   k=0
   fb=open('C:/Users/QA_Statistics_3.doc', 'wb')
   a=sorted(os.listdir(path))
   
   #k_w=0
   #k_o=0   
   for i in a[0:NNN]:
      print('# '+str(i))
      e=[]
      enc=0
      
      filename=path+'/'+str(i)


      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         #fb.write(bytes(str(i)+'; ', 'UTF-8')) 
         for line in file_object:
            line = line.rstrip('\n')
            a = line.strip()
            #print(a)
            
            if len(a)==0:
               enc=enc+1
  
            if enc==0:
            
               if len(line.strip())!=0:
                  
                  k=k+1
                  text=line.strip()
                  text=text.lower()
                  #print (text)
                  
                  text17=[]
                  text18=[]
                  text19=[]
                  text20=[]
                                    
                  filename1=str(i)
                  fb.write(bytes(str(filename1)+'; ', 'UTF-8'))
                  
                  #print(m)
                  da={}
                  ds={}
                  dv={}
                  d={}
                  b=[]
                  oo17=[]
                  oo18=[]
                  oo19=[]
                  oo20=[]
                  yy=[]

# STAGE 3.1 Find and Count the number of words in the Task that match the QA SubTasks Typology Vocabulary Keywords
#___________________QA Subtasks__________________________________________________________________________________                  

                  #_______4EP________
                     ff17=len(s17)
 
                     ddd17=len(s17)-1
                     hh=np.arange(0, ddd17, 1)
                     for i in hh[0:ddd1]:
                        text17 = re.findall(s17[i], text)
                        if text17!=[]:
                           oo1.append(text17)
                                                             
                     a17=len(oo17)
 
                  except:
                     pass

                  #_______backup & health check________
                  try:
                     ff18=len(s18)
  
                     ddd18=len(s18)-1
                     hh=np.arange(0, ddd18, 1)
                     for i in hh[0:ddd18]:
                        text182 = re.findall(s18[i], text)
                        #print(text2)
                        if text18!=[]:
                           oo18.append(text18)
                                                             
                     a18=len(oo18)
  
                  except:
                     pass

                  #_______software monitoring________
                  try:
                     ff19=len(s19)
  
                     ddd19=len(s19)-1
                     hh=np.arange(0, ddd19, 1)
                     for i in hh[0:ddd19]:
                        text19 = re.findall(s19[i], text)
                        if text19!=[]:
                           oo19.append(text19)
                                                             
                     a19=len(oo19)
  
                  except:
                     pass
                  #_______update test________
                  try:
                     ff20=len(s20)
  
                     ddd20=len(s209)-1
                     hh=np.arange(0, ddd20, 1)
                     for i in hh[0:ddd20]:
                        text20 = re.findall(s20[i], text)
                        if text209!=[]:
                           oo20.append(text209)
                                                             
                     a20=len(oo20)
  
                  except:
                     pass

#_________STAGE 4.3. Writing of Matched words and their Number in the *.csv file______________
           
                     fb.write(bytes('File; 4EP; Words; Backup & health check; Words; Software monitoring; Words; Update test; Words'+'\n', 'UTF-8'))
                     fb.write(bytes(str(oo17)+';'+str(a17)+';'+str(oo18)+';'+str(a18)+';'+str(oo19)+';'+str(a19)+';'+str(oo20)+';'+str(a20), 'UTF-8'))
                     fb.write(bytes('\n', 'UTF-8'))
 
                     
   
   fb.close()   
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
