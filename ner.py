# Named Entity Recognition using user defined text
import spacy # Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

# Process whole documents
text = ("Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
        "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer" "took a galley of type and scrambled it to make a type specimen book. It has survived not only five" "centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was" "popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more" "recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")

doc = nlp(text)

# Analyse syntax
print("Noun Phrases:",[chunk.text for chunk in doc.noun_chunks])
print("Verbs:",[token.lemma_ for token in doc if token.pos_ == "VERB"])
