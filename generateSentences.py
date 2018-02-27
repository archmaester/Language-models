from __future__ import division
import pickle as pickle 
import random as random
import numpy

dir_name = 'gutenberg'

fp = open(dir_name+'/'+'bigram_dict','r')
bigram_dict = pickle.load(fp)
fp.close()

fp = open(dir_name+'/'+'raw_unigram','r')
unigram_dict = pickle.load(fp)
fp.close()

sentences = []

word1 = 'START2'

total_length = len(unigram_dict.keys())

for i in range(0,10):
    
    denom = sum(bigram_dict[word1].values())
    len1 =  len(bigram_dict[word1].keys())
    list1 = bigram_dict[word1].keys()
    
    prob_dist = [x /denom for x in bigram_dict[word1].values()]  
    k = numpy.random.choice(list1,1,prob_dist)

    word = "".join(k)
    
    while word == 'UNKNOWN' or word =='STOP1' or word == 'STOP2' or word =='START1' or word =='START2' :
        k = numpy.random.choice(list1,1,prob_dist)
        word = "".join(k)
    
    word1 = word 
    sentences.append(word1)
    
print ' '.join(sentences)

        
