# Kharagpur Data Science Hackathon 2026 – Track A
## Global Narrative Consistency Reasoning

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Supported-green.svg)

### Challenge
Determine whether a hypothetical character backstory is **globally consistent** with a long-form narrative (novel) by performing **evidence-grounded, causal reasoning** over extended contexts.

---

## 🎯 Problem Statement

**Given:**
- A complete novel (100k+ words, untruncated)
- A hypothetical backstory for a central character

**Predict:**
- `1` → Backstory is **consistent** with the narrative
- `0` → Backstory **contradicts** the narrative

**Challenges:**
- Long-context understanding (100k+ word novels)
- Temporal constraint tracking across narrative
- Causal and behavioral consistency verification

---

## 🏗️ Architecture

The system implements a **deterministic reasoning pipeline** with five stages:

| Stage | Component | Purpose |
|-------|-----------|---------|
| **1. Ingestion** | `ingestion.py` + Pathway | Schema-enforced novel loading, chunking without truncation |
| **2. Decomposition** | `backstory_parser.py` | Convert backstory into atomic, testable claims |
| **3. Retrieval** | `retrieval.py` | Find relevant narrative chunks for each claim |
| **4. Reasoning** | `reasoning.py` | Verify causal, behavioral, temporal constraints |
| **5. Aggregation** | `aggregator.py` | Combine claim-level results into binary prediction |

**Key Design:**
- ✅ Pathway for ingestion & long-context handling
- ✅ Pure Python for transparent, debuggable reasoning
- ✅ No LLM generation—only structured constraint verification

---

## 📁 Project Structure

```
kds-hackathon/
├── Dockerfile                 # Linux runtime for Pathway
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── src/
│   ├── main.py              # Entry point
│   ├── ingestion.py         # Novel loading via Pathway
│   ├── backstory_parser.py  # Backstory → atomic claims
│   ├── retrieval.py         # Evidence retrieval
│   ├── reasoning.py         # Constraint verification logic
│   ├── aggregator.py        # Final prediction aggregation
│   └── __pycache__/         # (auto-generated, .gitignored)
└── data/
    ├── novels/
    │   └── story_001.txt
    └── backstories/
        └── story_001_backstory.txt
```

---

## 🚀 Quick Start (Windows + Docker)

### Prerequisites
- **Windows 10/11** with Administrator access
- **Docker Desktop** for Windows (with WSL 2)

### Setup (5 minutes)

#### 1. Install Docker Desktop

1. Download from: https://www.docker.com/products/docker-desktop/
2. During installation, enable **WSL 2**
3. Restart your system
4. Verify in PowerShell:
   ```powershell
   docker --version
   ```

#### 2. Clone Repository
```powershell
git clone <REPOSITORY_URL>
cd kds-hackathon
```

#### 3. Build Docker Image (One-time, ~5–10 min)
```powershell
docker build -t kds_pathway .
```

#### 4. Run Inference
```powershell
docker run --rm kds_pathway
```

**Output:**
```
1  # Consistent backstory
```
or
```
0  # Contradictory backstory
```

### Development Mode (Hot Reload)
To test code changes without rebuilding:
```powershell
docker run --rm `
  -v ${PWD}/src:/app/src `
  -v ${PWD}/data:/app/data `
  kds_pathway
```

---

## ⚙️ Configuration

**Input Files:**
- Novel: `data/novels/story_001.txt`
- Backstory: `data/backstories/story_001_backstory.txt`

**To test with new stories:**
1. Add novel file to `data/novels/`
2. Add backstory file to `data/backstories/`
3. Update `src/main.py` with filenames
4. Re-run Docker container

---

## 📊 Output Format

**Current:** Binary prediction (0 or 1) to stdout

**Planned Enhancements:**
- CSV batch results (`results.csv`)
- Per-claim reasoning logs
- Confidence scores

📌 Design Choices

Pathway is used for schema-enforced ingestion and long-context handling.

Pure Python is used for reasoning to ensure transparency and debuggability.

The system prioritizes robust reasoning over generation, in line with Track A evaluation criteria.

📄 Output Format

Current output:

<binary_prediction>


Planned extension:

results.csv with predictions for multiple stories

👥 Team Collaboration

Docker ensures identical runtime across all machines

No local Python or Pathway installation required

Teammates only need Docker Desktop

🚀 Future Improvements

Enhanced causal and temporal reasoning

Confidence-weighted aggregation

CSV batch inference

Detailed rationale logging for report analysis

📜 License

This project is developed for Kharagpur Data Science Hackathon 2026.
