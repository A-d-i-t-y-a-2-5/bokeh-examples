from data_loader import convert_tsf_to_dataframe

df, frequency, forecast_horizon, contain_missing_values, contain_equal_length = (
    convert_tsf_to_dataframe(
        "data/raw/web_traffic_extended_dataset_with_missing_values.tsf"
    )
)

print(df.head())
print(df.info())
print(frequency, forecast_horizon, contain_missing_values, contain_equal_length)

df.to_csv(
    "data/processed/web_traffic_extended_dataset_with_missing_values.csv", index=False
)