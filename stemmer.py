#PorterStemmer
import nltk
from nltk.stem import PorterStemmer
word_stemmer = PorterStemmer()
print('PorterStemmer',':',word_stemmer.stem('singing')) 

#LancasterStemmer
from nltk.stem import LancasterStemmer
lanc_stemmer = LancasterStemmer()
print('LancasterStemmer',':',lanc_stemmer.stem('dancing'))

#RegexpStemmer
from nltk.stem import RegexpStemmer
reg_stemmer = RegexpStemmer('ing$|s$|e$|able$', min=4)
print('RegexpStemmer',':',reg_stemmer.stem('writing'))

#SnowballStemmer
from nltk.stem import SnowballStemmer
english_stemmer = SnowballStemmer('english')
print('EnglishStemmer',':',english_stemmer.stem('writing'))

#WordNetLemmatizer
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print("word :\tlemma")
print("rocks:",lemmatizer.lemmatize("rocks"))
print("corpora :", lemmatizer.lemmatize("corpora"))

print("better:",lemmatizer.lemmatize("better",pos="a"))
