from monik import *
from preprocessing import preprocessing as prep
from generateDict import generateDict as Dict
import os 
import pickle as pickle
import time 
import re
tic = time.time()

pp = prep()
dir_name = 'brown_gutenberg/'
file_name = 'brown_gutenberg'
pp.preprocessingCorpus(dir_name,file_name,2)

# dir_name = 'brown/'
# pp.preprocessingBrownCorpus(dir_name)

# print time.time() - tic 

# file_name = 'brown'
# pd = Dict()
# pd.generateUnigram(file_name)

# file_name = 'gutenberg'
# pd = Dict()
# pd.generateUnigram(file_name)

# # print time.time() - tic
# pd = Dict()
# pd.UnknownMapping('gutenberg')
# pd.UnknownMapping('brown')

# pd = Dict()
# file_name = 'gutenberg'
# pd.generateBigram(file_name)
# print time.time() - tic 
# pd.generateTrigram(file_name)
# print time.time() - tic 

# pd = Dict()
# file_name = 'brown'
# pd.generateBigram(file_name)
# print time.time() - tic 
# pd.generateTrigram(file_name)
# print time.time() - tic 

# pd = Dict()
# pd.UnknownFileChange('gutenberg','dev','')
# pd.UnknownFileChange('gutenberg','test','')
# pd.UnknownFileChange('brown','dev','')
# pd.UnknownFileChange('brown','test','')

