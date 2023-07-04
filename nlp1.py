import spacy
txt = "List is a ubiquitous data structure in the python programming language"

nlp = spacy.load('en_core_web_sm')
doc = nlp(txt)

stk=[]
for w in doc:
    if w.pos_ == 'NOUN' or w.pos_ == 'PROPN':
        stk.append(w.text)
    elif (w.head.pos_ == 'NOUN' or w.head.pos_ == 'PROPN') and (w in w.head.lefts):
        stk.append(w.text)
    elif stk:
        chunk = ''
        while stk:
            chunk = stk.pop() + ' ' + chunk 
        print(chunk.strip())


if stk:
    chunk = ''
    while stk:
        chunk = stk.pop() + ' ' + chunk
    print(chunk.strip())