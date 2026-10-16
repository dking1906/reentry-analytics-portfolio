# Recommended Tableau Calculated Fields

## Employment Rate
SUM([employed_at_followup]) / COUNT([participant_id])

## Stable Housing Rate (>6 months)
SUM(IF [months_in_stable_housing] > 6 THEN 1 ELSE 0 END) / COUNT([participant_id])

## Program Participation Impact
AVG(IF [housing_program_enrolled] = 1 THEN [months_in_stable_housing] END) - 
AVG(IF [housing_program_enrolled] = 0 THEN [months_in_stable_housing] END)

## Equity Gap Indicator
AVG(IF [race_ethnicity] = "Black" THEN [equity_barrier_index] END) - 
AVG(IF [race_ethnicity] = "White" THEN [equity_barrier_index] END)

## Wage Conditional on Employment
AVG(IF [employed_at_followup] = 1 THEN [hourly_wage] END)

## Training Intensity
IF [workforce_program_enrolled] = 1 THEN [training_hours] ELSE 0 END
