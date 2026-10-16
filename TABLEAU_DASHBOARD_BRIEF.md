# Tableau Dashboard Brief: Reentry Cohort Analytics

## Recommended Worksheets

### 1. Housing Stability Overview
- Dimensions: housing_status_at_release, housing_type_current, race_ethnicity
- Measures: AVG(months_in_stable_housing), AVG(eviction_risk_score)
- Filter: housing_program_enrolled

### 2. Workforce & Employment Outcomes
- Dimensions: education, race_ethnicity, workforce_program_enrolled
- Measures: AVG(hourly_wage), SUM(months_employed), % employed_at_followup
- Color: equity_barrier_index

### 3. Equity Lens
- Dimensions: race_ethnicity, gender, education
- Measures: AVG(equity_barrier_index), AVG(service_utilization_score)
- Dual axis or small multiples

### 4. Program Impact Comparison
- Group by housing_program_enrolled and workforce_program_enrolled
- Compare outcomes: months_in_stable_housing, employed_at_followup, recidivism_proxy

## Calculated Fields (Tableau)
- Employment Rate: SUM([employed_at_followup]) / COUNT([participant_id])
- Stable Housing Rate: SUM(IF [months_in_stable_housing] > 6 THEN 1 ELSE 0 END) / COUNT([participant_id])

## Publishing Notes
- Connect to reentry_cohort_synthetic.csv
- Set release_date as Date
- Extract recommended for performance
- Publish to Tableau Public under your profile
