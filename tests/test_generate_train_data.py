from tomba.generate_train_data import (
    generate_train_data_for_states,
    generate_label_data_for_states,
)
import pathlib


def test_generate_train_data_for_states():
    first_found_paragraph = (
        "Acre \u00e9 uma das 27 unidades federativas do Brasil.[9] "
        "Localiza-se no sudoeste da Regi\u00e3o Norte, fazendo divisa "
        "com duas unidades federativas: Amazonas ao norte e Rond\u00f4nia "
        "a leste; e faz fronteira com dois pa\u00edses: a Bol\u00edvia a "
        "sudeste e o Peru ao sul e a oeste.[10] Sua \u00e1rea \u00e9 de "
        "164\u00a0123,040\u00a0km\u00b2,[3] que equivale aproximadamente "
        "ao Nepal.[11] Essa \u00e1rea responde inferiormente a 2% de todo "
        "o pa\u00eds.[12] De acordo com os ge\u00f3grafos, se trata de um "
        "dos estados com menor densidade demogr\u00e1fica do Brasil e foi "
        "o mais recente que os brasileiros povoaram de maneira efetiva.[12] "
        "Nele localiza-se a extremidade ocidental do Brasil.[nota 1] "
        "A cidade onde est\u00e3o sediados os poderes executivo, legislativo "
        "e judici\u00e1rio estaduais \u00e9 a capital Rio Branco.[13] "
        "Outros munic\u00edpios com popula\u00e7\u00e3o superior a trinta "
        "mil habitantes s\u00e3o: Cruzeiro do Sul, Feij\u00f3, Sena "
        "Madureira e Tarauac\u00e1.[14]\n"
    )

    filepath = pathlib.Path("data/states_wikipedia_paragraphs.json")

    train_data = generate_train_data_for_states(filepath)

    expected_train_data_0 = {
        "label": "STATE",
        "start": 0,
        "end": 4,
        "string": first_found_paragraph,
    }
    expected_train_data_1 = {
        "label": "STATE",
        "start": 140,
        "end": 148,
        "string": first_found_paragraph,
    }

    assert train_data[0] == expected_train_data_0
    assert train_data[1] == expected_train_data_1


def test_generate_label_data_for_sates():
    filepath = pathlib.Path("data/states.json")

    train_data = generate_label_data_for_states(filepath)

    expected_labels = [
        {"label": "STATE", "pattern": "Acre", "id": "acre"},
        {"label": "STATE", "pattern": "AC", "id": "acre"},
    ]

    assert train_data[0] == expected_labels[0]
    assert train_data[1] == expected_labels[1]
