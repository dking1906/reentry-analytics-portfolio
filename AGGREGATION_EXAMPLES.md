# Sample Aggregation Queries (for Tableau or Python)

## Housing Program Impact
SELECT housing_program_enrolled, 
       AVG(months_in_stable_housing) as avg_stable_months,
       AVG(eviction_risk_score) as avg_risk
FROM reentry_cohort
GROUP BY housing_program_enrolled;

## Workforce by Education
SELECT education, 
       AVG(hourly_wage) as avg_wage,
       SUM(employed_at_followup)*1.0 / COUNT(*) as employment_rate
FROM reentry_cohort
GROUP BY education;

## Equity Barriers by Race
SELECT race_ethnicity, 
       AVG(equity_barrier_index) as avg_barrier,
       AVG(service_utilization_score) as avg_utilization
FROM reentry_cohort
GROUP BY race_ethnicity;
