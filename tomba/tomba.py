import pathlib

import spacy
from spacy.matcher import Matcher

root_dir = pathlib.Path(__file__).parent.parent
nlp = spacy.load(f"{root_dir}/models/pt_core_news_sm_addresses")

# TODO verificar melhor maneira de identificar abreviações

LOCATION_LABELS = ["CITY", "STATE", "ZIPCODE"]

# adiciona identificação de ceps
matcher = Matcher(nlp.vocab)
pattern_with_dot = [{"SHAPE": "dd."}, {"SHAPE": "ddd-ddd"}]  # 44.050-024
pattern_without_dot = [{"SHAPE": "dddd-ddd"}]  # 44050-024
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
                "end": span.end_char,
            }
        )

    for ent in doc.ents:
        if ent.label_ in LOCATION_LABELS:
            found.append(
                {
                    "type": ent.label_,
                    "start": ent.start_char,
                    "end": ent.end_char,
                }
            )

    return found
