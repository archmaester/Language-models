from model import model
from generateDict import generateDict as Dict

pp = model()
pp.train('gutenberg/',0)
pp.train('brown/',1)
pp.train('brown_gutenberg/',2)
