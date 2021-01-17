from tomba import find_locations
import pytest


@pytest.mark.parametrize("text,expected_locations", [
    (
        "Contratação de empresa de engenharia para executar obras de pavimentação em paralelepípedos em diversas ruas dos Conjuntos Feira VII, Fraternidade e Elza Azevedo, localizados no bairro Tomba, neste município.",
        {
            "neighborhoods": ["Tomba"],
            "location": ["Feira VII", "Fraternidade", "Elza Azevedo"]
        }
    ),
    (
        "Assim,  a  Feira  da  Estação  Nova,  maior  de  todas  as  que  acontecem  nos  bairros,  assim como a do Tomba e a da Cidade Nova (essas são as principais), nos últimos anos foram impulsionadas de tal sorte que se tornaram importantes polos da economia do município, tamanho movimento recebem aos finais de semana, a partir da tarde de sexta-feira.",
        {
            "neighborhoods": ["Tomba", "Cidade Nova"],
            "location": ["Feira da Estação Nova"]
        }
    ),
    (
        "LOCAL: Salão  de  Licitações,  na  Av.  Sampaio,  nº  344,  Centro,  Feira  de  Santana  - Bahia",
        {
            "addresses": [
                {"address": "Av.  Sampaio,  nº  344,  Centro,  Feira  de  Santana  - Bahia", "start": 0, "end": 100}
            ],
        }
    ),
    (
        "Nenhuma localização deve ser encontrada nesse texto.",
        {}
    )
])
def test_identify_locations(text, expected_locations):
    assert find_locations(text) == expected_locations
