import nltk
from nltk import tokenize
nltk.download('punkt_tab')
nltk.download('words')

para = "Hello! My name is Beena Kapadia. Today you'll be learning NLTK."
sents = tokenize.sent_tokenize(para)
print("\nsentence tokenization\n=========================\n",sents)

print("\nword tokenization\n======================\n")
for index in range(len(sents)):
    words = tokenize.word_tokenize(sents[index])
    print(words)

