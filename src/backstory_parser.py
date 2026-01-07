def extract_claims(backstory_text: str):
    """
    Convert free-form backstory into atomic, testable claims.
    """
    claims = []

    sentences = backstory_text.split(".")
    for s in sentences:
        s = s.strip()
        if not s:
            continue

        if "believe" in s or "belief" in s:
            claims.append({"type": "belief", "text": s})
        elif "fear" in s:
            claims.append({"type": "fear", "text": s})
        elif "goal" in s or "ambition" in s:
            claims.append({"type": "motivation", "text": s})
        else:
            claims.append({"type": "background", "text": s})

    return claims
