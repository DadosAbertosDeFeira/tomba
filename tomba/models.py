import json
from pathlib import Path

from spacy.lang.pt import Portuguese

"""
from spacy.pipeline import ____

# Create EntityRuler instance
ruler = EntityRuler(nlp)

# Define pattern for new entity
ruler.add_patterns([{"label": "PRODUCT", "pattern": ____}])

# Update existing pipeline
nlp.add_pipe(____, before="ner")
"""

nlp = Portuguese()

ruler = nlp.add_pipe("entity_ruler", before="ner").from_disk("data/jsonl/cities/cities.jsonl")

state_patterns = json.load(open("data/collected/states/states_label.json"))
ruler.add_patterns(state_patterns)

nlp.add_pipe(____, before="ner")

Path("models/").mkdir(parents=True, exist_ok=True)
nlp.to_disk("models/pt_core_news_sm_addresses")
