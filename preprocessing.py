# -*- coding: utf-8 -*-
#Importing the required libraries 
import string
import re
import os
import operator
import sys
import pickle
from  collections import Counter
from nltk.corpus import gutenberg
from nltk.corpus import brown

from sklearn.model_selection import train_test_split
class preprocessing:
    
    def preprocessingCorpus(self,dir_name,l):
        
        #Initializing the array\
        reload(sys)
        sys.setdefaultencoding("latin-1")
            
        sent_all = []
        unique_words = []
        words = []
    
        if l ==0:
            fieldids = gutenberg.fileids()
            sent_all = list(gutenberg.sents(fieldids))
        if l==1:
            fieldids = brown.fileids()
            sent_all = list(brown.sents(fieldids))
        if l==2 :
            fieldids = brown.fileids()
            sent_all = list(brown.sents(fieldids))
            fieldids = gutenberg.fileids()
            sent_all += list(gutenberg.sents(fieldids))
                        
        # Save entire corpus in sententence form
        file1 = open(dir_name+'/'+'sent_all', 'w')

        for word in sent_all:
            blah = ''
            for entry in word:
                blah +=entry + ' '
            file1.write("START1 "+"START2 "+blah+" STOP1" +" STOP2"+ "\n")
        file1.close()
        
        
        #Splittng into train test
        file1 = open(dir_name+'/'+'sent_all', 'r')
        lines = file1.readlines()
        file1.close()
        
        train, test = train_test_split(lines, train_size = 0.8)

        #Saving training data
        file1 = open(dir_name+'/'+'train_sent', 'w')
        for word in train:
                 word = word.replace('\n','')
                 file1.write(str(word)+"\n")
        file1.close()

        #Splitting into train and development set
        dev, test_final = train_test_split(test, train_size = 0.5)

    
        file1 = open(dir_name+'/'+'test_sent', 'w')

        for word in test_final:
                word = word.replace('\n','')
                file1.write(str(word) + "\n")
        file1.close()

        file1 = open(dir_name+'/'+'dev_sent', 'w')

        for word in dev:
                 word = word.replace('\n','')
                 file1.write(str(word) + "\n")
        file1.close()

        #Collecting all words in the corpus 
        all_words = []

        for sent1 in train:
            words_list = sent1.split()
            all_words += words_list


        fp = open(dir_name+'/'+'all_words', 'w')
        pickle.dump(all_words, fp)
        fp.close()
        






    
    
    


