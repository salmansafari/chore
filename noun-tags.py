import nltk
from collections import defaultdict
nltk.download('averaged_perceptron_tagger_eng')
text = nltk.word_tokenize("I like to play cricket. Kohli is my favorite.")
tagged = nltk.pos_tag(text)
print(tagged)

addNounwords = []
count = 0
for words in tagged:
    val = tagged[count][1]
    if(val == 'NN'or val == 'NNS' or val == 'NNPS' or val == 'NNP'):
        addNounwords.append(tagged[count][0])
    count+=1

print(addNounwords)

temp = defaultdict(int)

for sub in addNounwords:
    for wrd in sub.split():
        temp[wrd]+=1
    
res = max(temp, key=temp.get)

print("Word with maximum frequency:"+str(res))