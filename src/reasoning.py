def analyze_claim(claim, evidence_chunks):
    score = 0
    rationale = []

    for chunk in evidence_chunks:
        text = chunk["text"].lower()   # ✅ now a real string

        if "never" in claim["text"].lower() and "agreed" in text:
            score -= 2
            rationale.append("Hard contradiction found.")
        else:
            score += 0

    return {
        "claim": claim,
        "score": score,
        "rationale": rationale
    }
