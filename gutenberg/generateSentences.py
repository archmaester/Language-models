from __future__ import division
import pickle as pickle 
import random as random
import numpy

dir_name = 'gutenberg'
d = 0.9

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
    
    prob_dist = []

    for word in unigram_dict.keys():
        
        if bigram_dict[word1][word] !=0:
            prob_dist.append((bigram_dict[word1][word] -d )/ denom)
        else:        
            prob_dist.append(d *len1 / ((total_length -len1) * denom)) 
    
    k = numpy.random.choice(unigram_dict.keys(),1,prob_dist)
    
    word = "".join(k)
    
    while word == 'UNKNOWN':
        k = numpy.random.choice(unigram_dict.keys(),1,prob_dist)
        word = "".join(k)
    
    word1 = word 
    sentences.append(word1)
    
print ' '.join(sentences)

        
