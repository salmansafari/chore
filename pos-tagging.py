import nltk
from nltk import tokenize, tag, chunk

# Download required NLTK resources (run once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')
nltk.download('averaged_perceptron_tagger_eng')

# Sample paragraph
# para = "Hello! My name is Prasanna. Today we are learning Natural Language Processing."
para = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

#1. Sentence Tokenization
sents = tokenize.sent_tokenize(para)
print(f'Sentence Tokenization -> {sents}\n\n')

#2. Word Tokenization
count = 0
for sent in sents:
    words = tokenize.word_tokenize(sent)
    print(f'Word Tokenization {count} -> {words}\n\n')
    count=count+1

#3. POS(Part-Of-Speech) Tagging
tagged_words = []
for index in range(len(sents)):
    tagged_words.append(tag.pos_tag(words))
    print(f'POS-Tagging -> {tagged_words}\n\n')

#4. Chunking
tree = []
for index in range(len(sents)):
    tree.append(chunk.ne_chunk(tagged_words[index]))
    print(f'Chunking -> {tree}\n\n')




