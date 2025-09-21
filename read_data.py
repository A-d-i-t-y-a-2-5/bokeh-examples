import pandas as pd

df = pd.read_pickle("data/processed/web_traffic.pkl")

df = df.sample(n=10000, random_state=42).reset_index(drop=True)
df.to_pickle("data/processed/10000/web_traffic_sample.pkl")