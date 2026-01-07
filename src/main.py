from ingestion import load_novel
from backstory_parser import extract_claims
from retrieval import build_vector_store, retrieve_evidence
from reasoning import analyze_claim
from aggregator import aggregate
from pathlib import Path


def run(story_id):
    novel_path = f"data/novels/story_{story_id}.txt"
    backstory_path = f"data/backstories/story_{story_id}_backstory.txt"

    # 1️⃣ Load novel using Pathway (schema + ingestion)
    novel_table = load_novel(novel_path)

    # 2️⃣ Materialize Pathway table ONCE into Python
    chunks = build_vector_store(novel_table)

    # 3️⃣ Read backstory
    backstory = Path(backstory_path).read_text(encoding="utf-8")
    claims = extract_claims(backstory)

    claim_results = []

    # 4️⃣ For each claim → retrieve evidence → analyze
    for claim in claims:
        evidence = retrieve_evidence(chunks, claim["text"])
        result = analyze_claim(claim, evidence)
        claim_results.append(result)

    # 5️⃣ Aggregate claim-level decisions
    prediction = aggregate(claim_results)
    return prediction


if __name__ == "__main__":
    print(run("001"))
