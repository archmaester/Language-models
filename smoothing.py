from __future__ import division
import math 
import pickle as pickle
import time 
        
class smoothing:
    def LinearInterpolation(self,dir_name,dir_name1,filename,gamma):
        
        fp = open(dir_name1+'/'+filename+'_sent','r')
        corpus = fp.readlines()        
        fp.close()
        
        dev_words = []
        
        for sent1 in corpus: 
            words_list = sent1.split()
            dev_words += words_list

            
        fp = open(dir_name+'/'+'raw_unigram','r')
        unigram_dict = pickle.load(fp)
        fp.close()
        
        fp = open(dir_name+'/'+'bigram_dict','r')
        bigram_dict = pickle.load(fp)
        fp.close()
        
        fp = open(dir_name+'/'+'trigram_dict','r')
        trigram_dict = pickle.load(fp)
        fp.close()
                
        trigram_list = []
        
        for i in range(len(dev_words)):
             if i < len(dev_words)-2:
                    trigram_list.append([dev_words[i],dev_words[i+1],dev_words[i+2]])
        log_prob = 0          
        
        for word1,word2,word3 in trigram_list:
            
            if unigram_dict[word1] == 0 :
                word1 = 'UNKNOWN'
            if unigram_dict[word2] == 0: 
                word2 = 'UNKNOWN'
            if unigram_dict[word3] == 0: 
                word3 = 'UNKNOWN'   
            
            lambda1 = 0
            lambda2 = 0 
            lambda3 = 0 
            prob_uni = 0 
            prob_bi = 0 
            prob_tri = 0
            
            
            if trigram_dict[word1][word2][word3] != 0:
                prob_tri = trigram_dict[word1][word2][word3]/bigram_dict[word1][word2]

            if bigram_dict[word2][word3] != 0:
                prob_bi = bigram_dict[word2][word3]/unigram_dict[word2]
            
            prob_uni = unigram_dict[word3]/sum(unigram_dict.values())
                        
            if bigram_dict[word1][word2] != 0: 
                lambda1 = bigram_dict[word1][word2]/(bigram_dict[word1][word2]+gamma)
            
            
            lambda2 = (1-lambda1)*unigram_dict[word2]/(unigram_dict[word2]+gamma)
            
            lambda3 = 1 - lambda1 - lambda2
             
            prob = lambda1*prob_tri + lambda2*prob_bi +lambda3*prob_uni 
            
            log_prob += math.log(prob)/math.log(2)
            
        return  2**(-log_prob/len(dev_words))  
    
    
    
    def BigramKneiserNay1(self,dir_name,dir_name1,target,d):
         
        fp = open(dir_name1+'/'+target+'_sent','r')
        corpus = fp.readlines()        
        fp.close()
        
        dev_words = []
        
        for sent1 in corpus: 
            words_list = sent1.split()
            dev_words += words_list

        
        fp = open(dir_name+'/'+'raw_unigram','r')
        unigram_dict = pickle.load(fp)
        fp.close()
        
        fp = open(dir_name+'/'+'bigram_dict','r')
        bigram_dict = pickle.load(fp)
        fp.close()
         
        fp = open(dir_name+'/'+'reverse_bigram_dict','r')
        reverse_bigram_dict = pickle.load(fp)
        fp.close()
             
        total_bigrams = 0 
        
        for word1 in bigram_dict.keys():
            total_bigrams += len(bigram_dict[word1].keys())
            
        bigram_list = []

        for i in range(len(dev_words)):
            
            if i < len(dev_words)-1:
                    bigram_list.append([dev_words[i],dev_words[i+1]])
             
        log_prob = 0
        
        for word1,word2 in bigram_list:
            
            prob_discount_word2 = 0 
            
            lambda_word1 = 0 
            
            p_word1 = 0 
             
            if unigram_dict[word1] == 0 :
                word1 = 'UNKNOWN'
            if unigram_dict[word2] == 0: 
                word2 = 'UNKNOWN'
                
                
            prob_discount_word2 = (bigram_dict[word1][word2]-d)/unigram_dict[word1]
            
            
            if prob_discount_word2 < 0 :
                prob_discount_word2 = 0 
                
            lambda_word1 = d*(len(bigram_dict[word1].keys())) / (sum(bigram_dict[word1].values()))
            
            p_word1 = len(reverse_bigram_dict[word2].keys())/ total_bigrams                                                     
            prob = prob_discount_word2 + lambda_word1*p_word1 
            
            log_prob += math.log(prob)/math.log(2)

        return  2**(-log_prob/len(dev_words))  
        
