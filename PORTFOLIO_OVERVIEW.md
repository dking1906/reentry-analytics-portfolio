# Portfolio Structure Overview

## Core Assets
- generate_reentry_data.py — Full cohort generator
- reentry_cohort_synthetic.csv (generated on demand)
- housing_stability_cohort.csv
- workforce_outcomes_cohort.csv

## Documentation
- README.md
- DATA_DICTIONARY.md
- TABLEAU_DASHBOARD_BRIEF.md
- CALCULATED_FIELDS.md
- OPERATIONALIZATION.md

## Automation
- .github/workflows/generate-and-publish.yml
- requirements.txt

## Usage
1. Generate or download CSVs
2. Connect in Tableau Public
3. Apply calculated fields from CALCULATED_FIELDS.md
4. Build dashboards per TABLEAU_DASHBOARD_BRIEF.md
