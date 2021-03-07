import json
from pathlib import Path

from spacy.lang.pt import Portuguese

nlp = Portuguese()

ruler = nlp.add_pipe("entity_ruler")
patterns = json.load(open("data/states/states_label.json"))

ruler.add_patterns(patterns)

Path("models/").mkdir(parents=True, exist_ok=True)
nlp.to_disk("models/pt_core_news_sm_addresses")
