from spacy.lang.zh import Chinese
import pdb

nlp = Chinese()
doc = nlp(u'我有分身無數，看哪個才是真的我？')
pdb.set_trace()