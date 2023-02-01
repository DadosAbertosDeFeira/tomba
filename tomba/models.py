import json
from pathlib import Path

from spacy.lang.pt import Portuguese

nlp = Portuguese()

ruler = nlp.add_pipe("entity_ruler").from_disk("data/jsonl/cities/cities.jsonl")

state_patterns = json.load(open("data/collected/states/states_label.json"))
ruler.add_patterns(state_patterns)

Path("models/").mkdir(parents=True, exist_ok=True)
nlp.to_disk("models/pt_core_news_sm_addresses")
