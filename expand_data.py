import pandas as pd

df = pd.read_csv("data/processed/500/web_traffic_sample.csv")

df["series_value"] = df["series_value"].str.replace("<NumpyExtensionArray>\n", "")

print(df["series_value"].iloc[0])