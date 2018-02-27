from preprocessing import preprocessing as prep
from smoothing import smoothing as smooth
from generateDict import generateDict as Dict

class model:
    
    def train(self,dir_name,l):
        
        pp = prep()
        pp.preprocessingCorpus(dir_name,l)
        
        pd = Dict()
        pd.generateUnigram(dir_name)
        pd.UnknownMapping(dir_name)
        pd.generateBigram(dir_name)
        pd.generateTrigram(dir_name)
        
        
    def test(self,dir_name,dir_name1,gamma,d,filename):
        
        
        #Tuning Parameters
        
        pp = smooth()

        perplexity = []
        
        perplexity.append(pp.LinearInterpolation(dir_name,dir_name1,filename,gamma))
        perplexity.append(pp.BigramKneiserNay1(dir_name,dir_name1,filename,d))
                                                       
        return perplexity 
