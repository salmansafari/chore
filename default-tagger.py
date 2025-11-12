import warnings
warnings.filterwarnings('ignore',category=DeprecationWarning)
import nltk
from nltk.tag import DefaultTagger
exptagger = DefaultTagger('NN')
from nltk.corpus import treebank
testsentences = treebank.tagged_sents()[1000:] 
print(exptagger.evaluate(testsentences))
print(exptagger.tag_sents([['Hi',','],['How','are','you','?']]))

