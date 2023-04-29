# tomba

[![Built with spaCy](https://img.shields.io/badge/made%20with%20❤%20and-spaCy-09a3d5.svg)](https://spacy.io)
[![CI](https://github.com/DadosAbertosDeFeira/tomba/actions/workflows/ci.yml/badge.svg)](https://github.com/DadosAbertosDeFeira/tomba/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/tomba.svg)](https://badge.fury.io/py/tomba)

Identifique endereços, bairros e outras localizações brasileiras em um texto. 🏘

Não sabe o que é o [Tomba](https://pt.wikipedia.org/wiki/Tomba_(Feira_de_Santana))?

---

:warning:️ Essa biblioteca é experimental e está no seu estágio inicial de desenvolvimento.

Objetivo:

```python
import tomba


tomba.get_locations(
    "Contratação de empresa de engenharia para executar obras "
    "de pavimentação localizados no CEP 44100-000, no bairro Tomba."
)
```

Saída:

```
[
    {"type": "zipcode", "start": 92, "end": 123},
    {"type": "neighborhood", "start": 113, "end": 118}
]
```

Suportando atualmente:

Endereços

- [ ] Endereços
- [ ] Bairros
- [x] CEPs
- [ ] Coordenadas
- [x] Cidades
- [x] Estados

## Desenvolvimento

Utilizamos o [poetry](https://python-poetry.org/) para empacotamento e gerenciamento das dependências.

Para instalar as dependências, execute `poetry install`.

Para configurar o [spacy](https://spacy.io) em português, execute:

```
poetry run python -m spacy download pt_core_news_sm
```

Para rodar os testes:

```
poetry run pytest
```

Para gerar um novo modelo:

```
poetry run python tomba/models.py
```
