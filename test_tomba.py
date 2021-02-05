from tomba import get_locations
import pytest


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
        ("Nenhuma localização deve ser encontrada nesse texto.", []),
    ],
)
def test_identify_locations(text, expected_locations):
    assert get_locations(text) == expected_locations
