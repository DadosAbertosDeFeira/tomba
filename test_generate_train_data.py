from generate_train_data import generate_train_data_for_states, generate_label_data_for_states
import pathlib


def test_generate_train_data_for_states():
    filepath = pathlib.Path("data/states_wikipedia_paragraphs.json")

    train_data = generate_train_data_for_states(filepath)

    expected_train_data = {
        "label": "STATE",
        "start": 0,
        "end": 3
    }

    {"label": "STATE", "pattern": "Apple", "id": "apple"}

    assert train_data[0] == expected_train_data


def test_generate_label_data_for_sates():
    filepath = pathlib.Path("data/states.json")

    train_data = generate_label_data_for_states(filepath)

    expected_labels = [{
        "label": "STATE",
        "pattern": "Acre",
        "id": "acre"
    },{
        "label": "STATE",
        "pattern": "AC",
        "id": "acre"
    },
    ]

    assert train_data[0] == expected_labels[0]
    assert train_data[1] == expected_labels[1]
