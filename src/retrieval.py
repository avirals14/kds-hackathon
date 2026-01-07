import pathway as pw


def build_vector_store(chunks_table):
    """
    Materialize Pathway table into Python dicts (stable API).
    """
    df = pw.debug.table_to_pandas(chunks_table)
    return df.to_dict(orient="records")


def retrieve_evidence(chunks, claim_text, k=5):
    """
    Pure Python keyword-based retrieval.
    """
    keywords = claim_text.lower().split()
    scored = []

    for chunk in chunks:
        text = chunk["text"].lower()
        score = sum(1 for kw in keywords if kw in text)
        if score > 0:
            scored.append((score, chunk))

    scored.sort(reverse=True, key=lambda x: x[0])

    if not scored:
        return chunks[:k]

    return [c for _, c in scored[:k]]
