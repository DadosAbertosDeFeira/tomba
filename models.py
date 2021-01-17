import spacy
import random


TRAIN_DATA = [
    ("Uber blew through $1 million a week", {"entities": [(0, 4, "ORG")]}),
    ("Google rebrands its business apps", {"entities": [(0, 6, "ORG")]})
]  # TODO melhorar exemplos de treino

nlp = spacy.blank("pt")
optimizer = nlp.begin_training()
for i in range(20):
    random.shuffle(TRAIN_DATA)
    for text, annotations in TRAIN_DATA:
        nlp.update([text], [annotations], sgd=optimizer)
nlp.to_disk("models/")
