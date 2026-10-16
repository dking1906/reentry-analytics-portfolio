"""
Synthetic Reentry Cohort Data Generator
Housing & Workforce Outcomes for Tableau Portfolio
"""
import pandas as pd
import numpy as np

def generate_reentry_cohort(n=5000, seed=42):
    np.random.seed(seed)
    
    participant_id = [f"R{str(i).zfill(5)}" for i in range(1, n+1)]
    age = np.random.normal(35, 10, n).clip(18, 65).astype(int)
    gender = np.random.choice(["Male", "Female", "Non-binary"], n, p=[0.65, 0.32, 0.03])
    race_ethnicity = np.random.choice(["Black", "White", "Hispanic", "Asian", "Other"], n, p=[0.45, 0.30, 0.18, 0.04, 0.03])
    education = np.random.choice(["Less than HS", "HS/GED", "Some College", "College+"], n, p=[0.25, 0.40, 0.25, 0.10])
    
    release_date = pd.to_datetime("2022-01-01") + pd.to_timedelta(np.random.randint(0, 730, n), unit="D")
    followup_months = np.random.randint(6, 25, n)
    
    housing_status_at_release = np.random.choice(["Homeless", "Unstable", "Stable", "Transitional"], n, p=[0.20, 0.35, 0.30, 0.15])
    housing_program_enrolled = np.random.choice([0, 1], n, p=[0.45, 0.55])
    housing_type_current = np.random.choice(["Street/Shelter", "Doubled-up", "Rental", "Own", "Transitional Housing"], n, p=[0.12, 0.25, 0.40, 0.10, 0.13])
    
    stable_mask = pd.Series(housing_type_current).isin(["Rental", "Own"])
    months_in_stable_housing = np.where(stable_mask, np.random.randint(1, 25, n), np.random.randint(0, 8, n))
    eviction_risk_score = np.random.beta(2, 5, n).round(2)
    
    workforce_program_enrolled = np.random.choice([0, 1], n, p=[0.40, 0.60])
    training_hours = np.where(workforce_program_enrolled == 1, np.random.gamma(2, 40, n).astype(int), 0)
    employed_at_followup = np.random.choice([0, 1], n, p=[0.45, 0.55])
    hourly_wage = np.where(employed_at_followup == 1, np.random.normal(16.5, 4.5, n).clip(10, 35).round(2), 0.0)
    months_employed = np.where(employed_at_followup == 1, np.random.randint(1, followup_months+1), 0)
    
    recidivism_proxy = np.random.choice([0, 1], n, p=[0.78, 0.22])
    service_utilization_score = np.random.beta(3, 2, n).round(2)
    equity_barrier_index = (np.random.beta(2.5, 3, n) * 100).round(1)
    
    return pd.DataFrame({
        "participant_id": participant_id,
        "age": age,
        "gender": gender,
        "race_ethnicity": race_ethnicity,
        "education": education,
        "release_date": release_date.strftime("%Y-%m-%d"),
        "followup_months": followup_months,
        "housing_status_at_release": housing_status_at_release,
        "housing_program_enrolled": housing_program_enrolled,
        "housing_type_current": housing_type_current,
        "months_in_stable_housing": months_in_stable_housing,
        "eviction_risk_score": eviction_risk_score,
        "workforce_program_enrolled": workforce_program_enrolled,
        "training_hours": training_hours,
        "employed_at_followup": employed_at_followup,
        "hourly_wage": hourly_wage,
        "months_employed": months_employed,
        "recidivism_proxy": recidivism_proxy,
        "service_utilization_score": service_utilization_score,
        "equity_barrier_index": equity_barrier_index
    })

if __name__ == "__main__":
    df = generate_reentry_cohort()
    df.to_csv("reentry_cohort_synthetic.csv", index=False)
    print(f"Wrote {len(df)} rows to reentry_cohort_synthetic.csv")
