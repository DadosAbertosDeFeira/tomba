from tomba.tomba import get_locations
import pytest


@pytest.mark.parametrize(
    "text,expected_locations",
    [
        (
            "A disputa pelo Acre n\u00e3o limitou-se \u00e0 esfera jur\u00eddica da "
            "aplica\u00e7\u00e3o de tratados e teve uma dimens\u00e3o de interesses "
            "pol\u00edticos e geo-estrat\u00e9gicos importantes:[46] para a "
            "conclus\u00e3o das fronteiras, para as rela\u00e7\u00f5es do Brasil com "
            "os Estados Unidos, para a prote\u00e7\u00e3o de brasileiros em "
            "territ\u00f3rio at\u00e9 ent\u00e3o estrangeiro, \u00e0 import\u00e2ncia"
            " da regi\u00e3o amaz\u00f4nica e, na orienta\u00e7\u00e3o da "
            "pol\u00edtica externa brasileira.[46] A Quest\u00e3o foi resolvida com "
            "diplomacia e n\u00e3o pelas armas, como esperava o Presidente "
            "Get\u00falio Vargas.[45] As cidades deste novo Estado foram ent\u00e3o "
            "nomeadas com nome dos solucionadores da Quest\u00e3o AC em homenagens "
            "p\u00f3stumas,[44][47] a capital recebeu o nome de Rio Branco e dois "
            "munic\u00edpios receberam o nome de Assis Brasil e Pl\u00e1cido de Castro.",
            [
                {"type": "state", "start": 15, "end": 19},  # Acre
                {"type": "state", "start": 590, "end": 592},  # AC
            ]
        ),
        (
            "Alagoas \u00e9 uma das 27 unidades federativas do Brasil. Est\u00e1 "
            "situado no leste da regi\u00e3o Nordeste e tem como limites Pernambuco "
            "(N e NO), Sergipe (S), Bahia (SO) e o Oceano Atl\u00e2ntico (L). Ocupa "
            "uma \u00e1rea de 27\u00a0778,506\u00a0km\u00b2, sendo ligeiramente "
            "maior que o Haiti. Sua capital \u00e9 Macei\u00f3 e a sede administrativa"
            " \u00e9 o Pal\u00e1cio Rep\u00fablica dos Palmares. O atual governador "
            "\u00e9 Renan Filho (MDB).",
            [
                {"type": "state", "start": 0, "end": 7},  # Alagoas
                {"type": "state", "start": 113, "end": 123},  # Pernambuco
                {"type": "state", "start": 134, "end": 141},  # Sergipe
                {"type": "state", "start": 147, "end": 152},  # Bahia
            ]
        )
    ]
)
def test_identify_states(text, expected_locations):
    assert get_locations(text) == expected_locations


@pytest.mark.skip
@pytest.mark.parametrize(
    "text,expected_locations",
    [
        (
            "Coordenadas geográficas de Feira de Santana, Brasil"
            "Latitude: 12°16′00″ S Longitude: 38°58′00″ O"
            "Altitude do nível do mar: 223 m\nCoordenadas por cidade"
            "Coordenadas de Feira de Santana em graus decimais"
            "Latitude: -12.2666700° Longitude: -38.9666700°"
            "Coordenadas de Feira de Santana em graus e minutos decimais"
            "Latitude: 12°16.0002′ S Longitude: 38°58.0002′ O",
            [
                {"type": "city", "start": 113, "end": 118},  # Feira de Santana
                {"type": "country", "start": 113, "end": 118},  # Brasil
                {"type": "coordinates", "start": 92, "end": 123},  # 12°16′00″ S, 38°58′00″ O
                {"type": "city", "start": 113, "end": 118},  # Feira de Santana
                {"type": "coordinates", "start": 92, "end": 123},  # -12.2666700°, -38.9666700°
                {"type": "city", "start": 113, "end": 118},  # Feira de Santana
                {"type": "coordinates", "start": 92, "end": 123},  # 12°16.0002′ S, 38°58.0002′ O
            ],
        ),
        (
            "Assim, a Feira da Estação Nova, maior de todas as que acontecem nos "
            "bairros, assim como a do Tomba e a da Cidade Nova (essas são as "
            "principais), nos últimos anos foram impulsionadas de tal sorte que "
            "se tornaram importantes polos da economia do município, tamanho "
            "movimento recebem aos finais de semana, a partir da tarde de "
            "sexta-feira.",
            [
                {"type": "neighborhood", "start": 92, "end": 123},  # Estação Nova
                {"type": "neighborhood", "start": 92, "end": 123},  # Tomba
                {"type": "neighborhood", "start": 92, "end": 123},  # Cidade Nova
            ],
        ),
        (
            "LOCAL: Salão de Licitações, na Av. Sampaio, nº 344, Centro, "
            "CEP 44100-000, Feira de Santana - Bahia",
            [
                {"type": "street", "start": 92, "end": 123},  # Av. Sampaio
                {"type": "number", "start": 92, "end": 123},  # nº 344
                {"type": "neighborhood", "start": 92, "end": 123},  # Centro
                {"type": "zipcode", "start": 113, "end": 118},  # 44100-000
                {"type": "city", "start": 113, "end": 118},  # Feira de Santana
                {"type": "state", "start": 113, "end": 118},  # Bahia
            ],
        ),
        (
            "LOCAÇÃO DE IMÓVEL SITUADO À RUA PARIS, Nº 97, BAIRRO SANTA MÔNICA, "
            "PARA O FUNCIONAMENTO DO CENTRO DE REFERÊNCIA DA MULHER MARIA QUITÉRIA, "
            "PELO PERÍODO DE 12 (DOZE) MESES, COORDENADO PELA SECRETARIA MUNICIPAL "
            "DE DESENVOLVIMENTO SOCIAL",
            [
                {"type": "street", "start": 92, "end": 123},  # RUA PARIS
                {"type": "number", "start": 92, "end": 123},  # Nº 97
                {"type": "neighborhood", "start": 92, "end": 123},  # SANTA MÔNICA
            ],
        ),
        ("Nenhuma localização deve ser encontrada nesse texto.", []),
    ],
)
def test_identify_locations(text, expected_locations):
    assert get_locations(text) == expected_locations
