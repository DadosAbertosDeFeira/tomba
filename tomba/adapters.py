import json
from pathlib import Path
from typing import List


def to_jsonl(pattern_list: List[dict], destination: Path, filename: str):
    if not filename.endswith(".jsonl"):
        filename = f"{filename}.jsonl"

    filepath = destination / filename
    content = "\n".join([json.dumps(pattern) for pattern in pattern_list])
    filepath.write_text(content)
