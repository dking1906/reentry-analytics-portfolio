# Reentry Analytics Portfolio
## Structured Synthetic Cohort for Agent-Assisted and Human-in-the-Loop Analysis

**Purpose**: Reproducible synthetic reentry cohort (housing stability, workforce outcomes, equity barriers) designed so that an analyst or agent can work with clear variables, documented relationships, and evaluation logic.

**Rows**: 5,000 participants (main cohort); additional domain-specific cohorts available via generators.

**Domains**: Housing stability, workforce development, employment outcomes, equity barriers.

### Why this exists
In environments where AI systems can generate and query analysis, the scarce capability is the ability to structure a data product so that outputs remain interpretable, equity-aware, and governable. This repository demonstrates that design step: transparent generators, explicit variable definitions, intended relationships, and calculated-field logic that can be applied by a human or an agent.

### Core assets
- `generate_reentry_data.py` — reproducible generator for the main cohort
- Data dictionaries, calculated-field definitions, relationship notes, and operationalization guidance
- Sample and domain-specific CSVs for immediate inspection

### Variables (main cohort)
See the table in the previous version or `DATA_DICTIONARY.md` for full definitions. Key fields include housing status and program enrollment, workforce program participation and outcomes, and a composite equity barrier index.

### Intended relationships (synthetic)
Program participation is associated with improved housing stability and employment metrics. The equity barrier index varies by demographic group and is inversely related to service utilization. These patterns are documented so that any analysis (human or agent-driven) can be evaluated against them.

### Usage
1. Clone the repository.
2. Run the generator or use the provided CSVs.
3. Apply the calculated fields and review the relationship notes before interpreting results.
4. The structure is tool-agnostic; it can feed Tableau, Python, or an agent querying a published extract.

### Notes
- Fully synthetic; no real individual records.
- Suitable for demonstrating data-product design, equity-aware evaluation logic, and HITL checkpoints.
- Not a substitute for administrative data or causal inference.

---
*Part of a scholar-practitioner portfolio focused on designing and governing analytical assets in public-sector and workforce contexts.*
