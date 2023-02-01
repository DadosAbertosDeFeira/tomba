from pathlib import Path

from tomba.adapters import to_jsonl


def test_to_jsonl(tmp_path):
    pattern_list = [
        {"label": "CITY", "pattern": "Amélia Rodrigues"},
        {"label": "CITY", "pattern": "Feira de Santana"},
        {"label": "CITY", "pattern": "Salvador"},
    ]
    destination = Path(tmp_path)
    filename = "cities.jsonl"
    expected_file = destination / filename
    expected_content = (
        '{"label": "CITY", "pattern": "Am\\u00e9lia Rodrigues"}\n'
        '{"label": "CITY", "pattern": "Feira de Santana"}\n'
        '{"label": "CITY", "pattern": "Salvador"}'
    )

    to_jsonl(pattern_list, destination, filename)

    assert expected_file.exists()
    assert expected_file.read_text() == expected_content
