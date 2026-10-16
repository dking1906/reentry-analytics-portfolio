"""
Quick analysis script for reentry portfolio datasets.
Run after generating CSVs.
"""
import pandas as pd

def load_and_summarize():
    try:
        full = pd.read_csv("reentry_cohort_synthetic.csv")
        print("Full cohort shape:", full.shape)
        print("Employment rate:", full["employed_at_followup"].mean())
        print("Avg stable housing months:", full["months_in_stable_housing"].mean())
    except FileNotFoundError:
        print("Run generate_reentry_data.py first")

    housing = pd.read_csv("housing_stability_cohort.csv")
    print("\nHousing cohort shape:", housing.shape)
    print("Program enrollment rate:", housing["housing_program_enrolled"].mean())

    workforce = pd.read_csv("workforce_outcomes_cohort.csv")
    print("\nWorkforce cohort shape:", workforce.shape)
    print("Placement rate:", workforce["placement_within_90_days"].mean())

if __name__ == "__main__":
    load_and_summarize()
