from model import model
import time 
from generateDict import generateDict as Dict

pp = model()
# pp.train('gutenberg/',0)
# pp.train('brown/',1)
# pp.train('brown_gutenberg/',2)

print "S1: Train: D1-Train, Test: D1-Test"
print "-------------------------------------"

tic = time.time()
perplexity = pp.test('brown/','brown/',100,0.9,'test')
print time.time() - tic
print 'The perplexity of Trigram with Linear Interpolation model is '+str(perplexity[0])
print 'The perplexity of Bigram with Kneser Nay model is '+str(perplexity[1])

print "\n"
print "S2: Train: D2-Train, Test: D2-Test"
print "-------------------------------------"

perplexity = pp.test('gutenberg/','gutenberg/',100,0.4,'test')
print time.time() - tic
print 'The perplexity of Trigram with Linear Interpolation model is '+str(perplexity[0])
print 'The perplexity of Bigram with Kneser Nay model is '+str(perplexity[1])

print "\n"
print "S3: Train: D1-Train + D2-Train, Test: D1-Test"
print "-------------------------------------"

perplexity = pp.test('brown_gutenberg/','brown/',200,0.4,'test')
print time.time() - tic
print 'The perplexity of Trigram with Linear Interpolation model is '+str(perplexity[0])
print 'The perplexity of Bigram with Kneser Nay model is '+str(perplexity[1])

print "\n"
print "S4: Train: D1-Train + D2-Train, Test: D2-Test"
print "-------------------------------------"

perplexity = pp.test('brown_gutenberg/','gutenberg/',150,0.4,'test')
print time.time() - tic
print 'The perplexity of Trigram with Linear Interpolation model is '+str(perplexity[0])
print 'The perplexity of Bigram with Kneser Nay model is '+str(perplexity[1])
print "\n"
print "\n"
