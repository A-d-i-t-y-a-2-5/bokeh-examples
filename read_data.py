import pandas as pd

df = pd.read_csv("data/processed/web_traffic_extended_dataset_with_missing_values.csv")

df = df.sample(n=10000, random_state=42).reset_index(drop=True)
df.to_csv("data/processed/10000/web_traffic_sample.csv", index=False)