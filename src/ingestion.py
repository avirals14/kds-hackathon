import pathway as pw
from pathlib import Path

class ChunkSchema(pw.Schema):
    chunk_id: int
    text: str
    start: int
    end: int


def load_novel(novel_path: str):
    text = Path(novel_path).read_text(encoding="utf-8")

    CHUNK_SIZE = 1000
    OVERLAP = 200

    rows = []
    start = 0
    idx = 0

    while start < len(text):
        end = start + CHUNK_SIZE
        rows.append((
            idx,
            text[start:end],
            start,
            end
        ))
        start += CHUNK_SIZE - OVERLAP
        idx += 1

    # ✅ CORRECT ORDER: schema FIRST, rows SECOND
    return pw.debug.table_from_rows(
        ChunkSchema,
        rows
    )
