def aggregate(claim_results):
    for cr in claim_results:
        if cr["score"] <= -2:
            return 0  # Contradiction

    return 1  # Consistent
