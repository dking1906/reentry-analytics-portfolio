# Reentry Cohort Synthetic Dataset
## Housing & Workforce Outcomes

**Purpose**: Tableau-ready synthetic dataset for DBA scholar-practitioner portfolio work in reentry analytics.  
**Rows**: 5,000 participants  
**Domains**: Housing stability, workforce development, employment outcomes, equity barriers  

### Variables
| Column | Type | Description |
|--------|------|-------------|
| participant_id | string | Unique ID (R00001–R05000) |
| age | int | Age at release (18–65) |
| gender | string | Male / Female / Non-binary |
| race_ethnicity | string | Black / White / Hispanic / Asian / Other |
| education | string | Less than HS / HS/GED / Some College / College+ |
| release_date | date | Simulated release date (2022–2023) |
| followup_months | int | Months of follow-up observation |
| housing_status_at_release | string | Homeless / Unstable / Stable / Transitional |
| housing_program_enrolled | int | 0/1 participation in housing program |
| housing_type_current | string | Street/Shelter / Doubled-up / Rental / Own / Transitional Housing |
| months_in_stable_housing | int | Months in rental or owned housing |
| eviction_risk_score | float | 0–1 continuous risk score |
| workforce_program_enrolled | int | 0/1 participation in workforce program |
| training_hours | int | Hours of training completed |
| employed_at_followup | int | 0/1 employed at follow-up |
| hourly_wage | float | Hourly wage if employed |
| months_employed | int | Months employed during follow-up |
| recidivism_proxy | int | 0/1 binary proxy outcome |
| service_utilization_score | float | 0–1 service engagement score |
| equity_barrier_index | float | 0–100 composite barrier index |

### Usage in Tableau
1. Download `reentry_cohort_synthetic.csv`
2. Connect to Text File in Tableau Public/Desktop
3. Suggested dimensions: race_ethnicity, education, housing_status_at_release, gender
4. Suggested measures: hourly_wage, months_in_stable_housing, eviction_risk_score, equity_barrier_index
5. Filters: housing_program_enrolled, workforce_program_enrolled, employed_at_followup

### Notes
- Fully synthetic; no real individual data.
- Variable relationships approximate real-world reentry patterns (program participation associated with better housing/employment outcomes).
- Suitable for equity analysis, program impact visualization, and dashboard prototyping.
