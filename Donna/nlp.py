import spacy

spacy_parser = spacy.load("en_core_web_sm")
from Donna import sentences


class Parser:
    def __init__(self):
        pass
    def parse(self, string):
        parsed_data = spacy_parser(string)
        dependency = {token.dep_:token.orth_ for token in parsed_data}
        direct_object = dependency.get("dobj")
        for np in parsed_data.noun_chunks :
            print(np.orth_)
            if dependency.get("dobj") in np.orth_:
                direct_object = np.orth_

        verb = dependency["ROOT"]
        return sentences.Sentence(verb, direct_object)


