import spacy

nlp = spacy.load("models/pt_core_news_sm_addresses")

# TODO verificar melhor maneira de identificar abreviações

LOCATION_LABELS = ["STATE"]


def get_locations(text):
    found = []
    doc = nlp(text)

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
