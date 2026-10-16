# Expanded Data Dictionary — Reentry Analytics Portfolio

## Housing Stability Cohort
| Field | Type | Description | Notes |
|-------|------|-------------|-------|
| participant_id | string | Unique identifier | Prefixed H |
| housing_status_at_release | categorical | Status at release | Homeless/Unstable/Stable/Transitional |
| housing_program_enrolled | binary | Enrolled in housing program | 0/1 |
| months_to_stable_housing | integer | Months until stable housing | Gamma distributed |
| eviction_events | integer | Number of eviction events | Poisson |
| housing_type_6mo | categorical | Housing type at 6 months | Street/Shelter etc. |
| rent_burden_ratio | float | Rent / income ratio | 0–1 |

## Workforce Outcomes Cohort
| Field | Type | Description | Notes |
|-------|------|-------------|-------|
| participant_id | string | Unique identifier | Prefixed W |
| training_completed | binary | Completed training | 0/1 |
| training_hours | integer | Hours of training | Gamma |
| placement_within_90_days | binary | Placed within 90 days | 0/1 |
| starting_wage | float | Starting hourly wage | Normal |
| retention_6mo | binary | Retained at 6 months | 0/1 |
| industry_sector | categorical | Sector of placement | Construction etc. |

## Original Reentry Cohort
See main README.md for the 20-column full cohort.
