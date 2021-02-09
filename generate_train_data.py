import httpx
from bs4 import BeautifulSoup
import json
import pathlib
from pprint import pprint

# TODO identifica o nome do estado no texto
# TODO gera o arquivo amigável para os dados de treino do spacy

states = json.load(open("data/states.json"))


def get_states_wikipedia_pages():
    response = httpx.get(
        "https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_popula%C3%A7%C3%A3o"
    )
    if response.status_code != 200:
        raise Exception(f"Falha ao acessar a Wikipedia {response}")

    soup = BeautifulSoup(response.text, features="html.parser")
    rows = soup.select("table.wikitable tr td a")
    for row in rows:
        title = row.get("title")
        title = title.replace(" (estado)", "").replace(" (Brasil)", "")
        if states.get(title):
            states[title][
                "wikipedia_url"
            ] = f"https://pt.wikipedia.org{row.get('href')}"
    return states


def generate_state_train_data(state_wikipedia_url):
    response = httpx.get(state_wikipedia_url)
    if response.status_code != 200:
        raise Exception(f"Falha ao acessar a Wikipedia {response}")

    soup = BeautifulSoup(response.text, features="html.parser")
    paragraphs = soup.select("div.mw-parser-output p")[:4]
    return [paragraph.text for paragraph in paragraphs]


def generate_train_data_for_states(filepath):
    states_with_paragraphs = json.load(open(filepath))
    for paragraph in states_with_paragraphs:
        # TODO find state in paragraph
        for state in states:
            pass


def generate_label_data_for_states(filepath):
    labels = []
    states_with_paragraphs = json.load(open(filepath))
    for state, data in states_with_paragraphs.items():
        labels.append({
            "label": "STATE",
            "pattern": state,
            "id": state.lower()
        })
        labels.append({
            "label": "STATE",
            "pattern": data["sigla"],
            "id": state.lower()
        })
    return labels


if __name__ == "__main__":
    # TODO transformar em uma CLI

    """
    filepath = pathlib.Path("data/states_wikipedia_paragraphs.json")
    if filepath.is_file():
        # TODO gera dados no formato do spacy
        generate_train_data_for_states(filepath)
    else:
        print("O arquivo não existe. Vamos fazer download de um novo.")

        wikipedia_pages = get_states_wikipedia_pages()
        paragraphs_by_state = wikipedia_pages.copy()
        for state, data in wikipedia_pages.items():
            print(state, data)
            paragraphs_by_state[state]["paragraphs"] = generate_state_train_data(
                data["wikipedia_url"]
            )

        with open("data/states_wikipedia_paragraphs.json", "w") as f:
            json.dump(paragraphs_by_state, f)
    """
    states_label = generate_label_data_for_states("data/states.json")
    with open("data/states_label.json", "w") as f:
        json.dump(states_label, f)
