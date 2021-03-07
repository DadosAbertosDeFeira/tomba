import argparse
import httpx
from bs4 import BeautifulSoup
import json
import pathlib
import re


root_dir = pathlib.Path(__file__).parent.parent
states = json.load(open(f"{root_dir}/data/states/states.json"))


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


def download_paragraphs_from_wikipedia_page(state_wikipedia_url):
    response = httpx.get(state_wikipedia_url)
    if response.status_code != 200:
        raise Exception(f"Falha ao acessar a Wikipedia {response}")

    soup = BeautifulSoup(response.text, features="html.parser")
    paragraphs = soup.select("div.mw-parser-output p")
    return [paragraph.text for paragraph in paragraphs]


def generate_train_data_for_states(filepath):
    states_with_paragraphs = json.load(open(filepath))
    labeled_data = []
    for paragraph in states_with_paragraphs:
        # naive approach
        for state in states:
            for match in re.finditer(state, paragraph):
                labeled_data.append(
                    {
                        "label": "STATE",
                        "start": match.start(),
                        "end": match.end(),
                        "string": match.string,
                    }
                )

    return labeled_data


def generate_label_data_for_states(filepath):
    labels = []
    states_with_paragraphs = json.load(open(filepath))
    for state, data in states_with_paragraphs.items():
        labels.append({"label": "STATE", "pattern": state, "id": state.lower()})
        labels.append({"label": "STATE", "pattern": data["sigla"], "id": state.lower()})
    return labels


if __name__ == "__main__":
    actions = ["entity_label", "download_wikipedia", "generate_train_data"]
    parser = argparse.ArgumentParser(description='Gera dados de treino.')
    parser.add_argument('entity', help='Qual o tipo de dado?')
    parser.add_argument('action', help=f'O que você deseja fazer? e.g. {actions}')
    parser.add_argument('--args', metavar='N', nargs='+', help='Argumentos')

    args = parser.parse_args()
    entity = args.entity
    action = args.action
    args = args.args

    if action not in actions:
        raise Exception(f"Ação inválida. Opções: {actions}")

    if entity == "estado":
        if action == "entity_label":
            # gera labels para estados
            if not args:
                json_file = f"{root_dir}/data/states/states.json"
            else:
                json_file = args[0]
            states_label = generate_label_data_for_states(json_file)
            with open(f"{root_dir}/data/states/states_label.json", "w") as f:
                json.dump(states_label, f, ensure_ascii=True, indent=4)
        elif action == "download_wikipedia":
            # baixa paragrafos sobre estados do wikipedia
            wikipedia_pages = get_states_wikipedia_pages()
            paragraphs_by_state = wikipedia_pages.copy()
            all_paragraphs = []
            for state, data in wikipedia_pages.items():
                print(state, data)
                paragraphs_by_state[state]["paragraphs"] = download_paragraphs_from_wikipedia_page(
                    data["wikipedia_url"]
                )
                all_paragraphs.extend(paragraphs_by_state[state]["paragraphs"])
            with open(f"{root_dir}/data/states/wikipedia_paragraphs_by_state.json", "w") as f:
                json.dump(paragraphs_by_state, f, ensure_ascii=True, indent=4)
            with open(f"{root_dir}/data/states/states_wikipedia_paragraphs.json", "w") as f:
                json.dump(all_paragraphs, f, ensure_ascii=True, indent=4)
        elif action == "generate_train_data":
            # gera dados de treino no formato do spacy
            filepath = pathlib.Path(f"{root_dir}/data/states/states_wikipedia_paragraphs.json")
            if filepath.is_file():
                labeled_data = generate_train_data_for_states(filepath)
                with open(f"{root_dir}/data/states/states_labeled_data.json", "w") as f:
                    json.dump(labeled_data, f, ensure_ascii=True, indent=4)
