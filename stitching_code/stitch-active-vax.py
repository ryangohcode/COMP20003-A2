import pandas as pd

VAX_RATES_PATH="../cleaned_datasets/vaccination_rates_by_lga.csv"
ACTIVE_CASES_PATH="../cleaned_datasets/active_cases_by_lga.csv"
POP_AGE_PATH="../cleaned_datasets/population_by_age_by_lga.csv"

vax_rates=pd.read_csv(VAX_RATES_PATH)
#print(vax_rates.to_string())

active_cases=pd.read_csv(ACTIVE_CASES_PATH)
#print(active_cases.to_string())

dataset = vax_rates.join(other=active_cases, lsuffix="", rsuffix="_ACTIVE_CASES", how='inner')
dataset = dataset[["LGA", "% Dose 1", "% Dose 2", "active-cases", "Population"]]
#dataset=pd.merge(vax_rates, active_cases, how='inner', left_on=['LGA'], right_on=['LGA'])
dataset["Population"] = dataset["Population"].map(lambda a: int(a.replace(',', '')))
dataset["active_cases_per_capita"] = dataset["active-cases"]/dataset["Population"]

max_val = dataset["active_cases_per_capita"].max()
dataset["active_cases_per_capita_norm"] = dataset["active_cases_per_capita"]/max_val

print(dataset.to_string())
dataset.to_csv('../stitched_datasets/vax-active-by-lga.csv', index=False)
