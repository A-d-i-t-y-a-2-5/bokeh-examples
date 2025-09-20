import pandas as pd

df = pd.read_parquet("data/processed/web_traffic.parquet")

print(df)