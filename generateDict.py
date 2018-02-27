from monik import *
import dill
import pickle as pickle
from  collections import Counter
from collections import defaultdict

class generateDict:
    def generateUnigram(self,dir_name):

        fp1 = open(dir_name+'/'+'all_words', 'r')
        all_words = pickle.load(fp1)
        fp1.close()

        #Dictionary to save count of words
        cnt = Counter()

        for word in all_words:
            cnt[word] += 1

        unique_words = cnt.keys()
        
        unknown_words = [] 
        count = 0
        for word in unique_words:
            if cnt[word] < 2 : 
                if count < 1000:
                    cnt['UNKNOWN'] += cnt[word]
                    del cnt[word] 
                    unknown_words.append(word)
                    count = count + 1
                    
       
        #Saving the final unique words and their counts
        fp = open(dir_name+'/'+'raw_unigram','w')
        pickle.dump(cnt,fp)
        fp.close()
        
        fp = open(dir_name+'/'+'unknown_list','w')
        pickle.dump(unknown_words,fp)
        fp.close()
    
    
    def generateBigram(self,dir_name):
        
        fp1 = open(dir_name+'/'+'all_words', 'r')
        all_words = pickle.load(fp1)
        fp1.close()

        bigram_list = []

        for i in range(len(all_words)):
            
            if i < len(all_words)-1:
                    bigram_list.append([all_words[i],all_words[i+1]])
            
        bigram_dict = defaultdict(lambda: defaultdict(lambda: 0))
        reverse_bigram_dict = defaultdict(lambda: defaultdict(lambda: 0))
        
        for w1,w2 in bigram_list:
                bigram_dict[w1][w2] += 1
                reverse_bigram_dict[w2][w1] = 1
        
        fp = open(dir_name+'/'+'bigram_dict','w')
        pickle.dump(bigram_dict,fp)
        fp.close()
        
        fp = open(dir_name+'/'+'reverse_bigram_dict','w')
        pickle.dump(reverse_bigram_dict,fp)
        fp.close()
        
    def generateTrigram(self,dir_name):
        
        fp1 = open(dir_name+'/'+'all_words', 'r')
        all_words = pickle.load(fp1)
        fp1.close()
        
        trigram_list = []
        for i in range(len(all_words)):
            if i < len(all_words)-2:
                trigram_list.append([all_words[i],all_words[i+1],all_words[i+2]])

        trigram_dict = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0)))
        
        
        for w1,w2,w3 in trigram_list:
            trigram_dict[w1][w2][w3] += 1
            
              
        fp = open(dir_name+'/'+'trigram_dict','w')
        pickle.dump(trigram_dict,fp)
        fp.close()
        
        
    def UnknownMapping(self,dir_name):
                #Initialize Bigrams and Trigrams 
        
        fp1 = open(dir_name+'/'+'all_words', 'r')
        all_words = pickle.load(fp1)
        fp1.close()

        sentences = ' '.join(word for word in all_words)

        fp = open(dir_name+'/'+'unknown_list','r')
        unknown_list = pickle.load(fp)
        fp.close()

        for item in unknown_list:
            sentences = sentences.replace(' '+ item+' ' ,' UNKNOWN ')


        all_words = sentences.split()    

        fp = open(dir_name+'/'+'all_words', 'w')
        pickle.dump(all_words, fp)
        fp.close()

        
    def UnknownFileChange(self,dir_name,dir_name1,name,name2):
        
        fp = open(dir_name+'/'+'raw_unigram','r')
        unigram_dict = pickle.load(fp)
        fp.close()

        fp = open(dir_name1+'/'+name+'_sent','r')
        corpus = fp.readlines()

        fp.close()

        dev_words = []
#         sentences = ''
        
        sentences = ' '.join(sent1 for sent1 in corpus)
             
#             dev_words += sent
#             words_list = sent1.split()
#             dev_words += words_list

#         for index,token in enumerate(dev_words):
#             if token not in unigram_dict.keys():
#                 dev_words[index] = 'UNKNOWN'
        
#         sentences = ' '.join(word for word in dev_words)

        for word in dev_words:
            if word not in unigram_dict.keys():
                sentences = sentences.replace(' '+word+' ',' UNKNOWN ')


        dev_words = sentences.split() 
        
        fp = open(dir_name+'/'+name2+'_words', 'w')
        pickle.dump(dev_words, fp)
        fp.close()
        

            