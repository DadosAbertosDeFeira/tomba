import spacy


nlp = spacy.load("models/pt_core_news_sm_addresses")

# TODO verificar melhor maneira de identificar abreviações

def get_locations(text):
    doc = nlp(text)

    #[(ent.text, ent.label_, ent.ent_id_) for ent in doc2.ents]
    return []
