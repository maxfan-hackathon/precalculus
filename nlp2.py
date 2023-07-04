import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp("The cat chased the mouse.")

for token in doc:
    print(token.text, token.head.text)
