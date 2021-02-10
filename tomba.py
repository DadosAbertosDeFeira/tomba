import json
from spacy.lang.pt import Portuguese


nlp = Portuguese()

ruler = nlp.add_pipe("entity_ruler")
patterns = json.load(open("data/states_label.json"))
ruler.add_patterns(patterns)

# TODO verificar como identificar abreviações

doc1 = nlp("A disputa pelo Acre n\u00e3o limitou-se \u00e0 esfera jur\u00eddica da aplica\u00e7\u00e3o de tratados e teve uma dimens\u00e3o de interesses pol\u00edticos e geo-estrat\u00e9gicos importantes:[46] para a conclus\u00e3o das fronteiras, para as rela\u00e7\u00f5es do Brasil com os Estados Unidos, para a prote\u00e7\u00e3o de brasileiros em territ\u00f3rio at\u00e9 ent\u00e3o estrangeiro, \u00e0 import\u00e2ncia da regi\u00e3o amaz\u00f4nica e, na orienta\u00e7\u00e3o da pol\u00edtica externa brasileira.[46] A Quest\u00e3o foi resolvida com diplomacia e n\u00e3o pelas armas, como esperava o Presidente Get\u00falio Vargas.[45] As cidades deste novo Estado foram ent\u00e3o nomeadas com nome dos solucionadores da Quest\u00e3o AC em homenagens p\u00f3stumas,[44][47] a capital recebeu o nome de Rio Branco e dois munic\u00edpios receberam o nome de Assis Brasil e Pl\u00e1cido de Castro.\n")
print([(ent.text, ent.label_, ent.ent_id_) for ent in doc1.ents])

doc2 = nlp("Alagoas \u00e9 uma das 27 unidades federativas do Brasil. Est\u00e1 situado no leste da regi\u00e3o Nordeste e tem como limites Pernambuco (N e NO), Sergipe (S), Bahia (SO) e o Oceano Atl\u00e2ntico (L). Ocupa uma \u00e1rea de 27\u00a0778,506\u00a0km\u00b2, sendo ligeiramente maior que o Haiti. Sua capital \u00e9 Macei\u00f3 e a sede administrativa \u00e9 o Pal\u00e1cio Rep\u00fablica dos Palmares. O atual governador \u00e9 Renan Filho (MDB).\n")
print([(ent.text, ent.label_, ent.ent_id_) for ent in doc2.ents])

def get_locations(text):
    return []
