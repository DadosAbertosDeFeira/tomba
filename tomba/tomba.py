import spacy
from spacy.matcher import Matcher

nlp = spacy.load("models/pt_core_news_sm_addresses")

# TODO verificar melhor maneira de identificar abreviações

LOCATION_LABELS = ["STATE", "ZIPCODE"]

# adiciona identificação de ceps
matcher = Matcher(nlp.vocab)
pattern_with_dot = [  # 44.050-024
    {"SHAPE": "dd."}, {"SHAPE": "ddd-ddd"}
]
pattern_without_dot = [  # 44050-024
    {"SHAPE": "dddd-ddd"}
]
matcher.add("ZIPCODE", [pattern_with_dot, pattern_without_dot])


def get_locations(text):
    found = []
    doc = nlp(text)

    matches = matcher(doc)
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]
        span = doc[start:end]
        found.append(
            {
                "type": string_id,
                "start": span.start_char,
                "end":span.end_char,
            }
        )

    for ent in doc.ents:
        if ent.label_ in LOCATION_LABELS:
            found.append(
                {
                    "type": ent.label_.lower(),  # TODO check how is the default
                    "start": ent.start_char,
                    "end": ent.end_char,
                }
            )

    return found
