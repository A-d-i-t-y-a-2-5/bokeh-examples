import argparse
import os
import pandas as pd


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--n-samples",
        type=int,
        default=500,
        help="Number of samples to extract from the dataset",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    df = pd.read_pickle(
        os.path.join("data", "processed", str(args.n_samples), "web_traffic_sample.pkl")
    )
    df["timestamps"] = df.apply(
        lambda row: pd.date_range(
            start=row["start_timestamp"], periods=len(row["series_value"]), freq="D"
        ),
        axis=1,
    )
    
    df = df[["series_name", "timestamps", "series_value"]]

    long_df = df.explode(["timestamps", "series_value"]).reset_index(drop=True)
    long_df["series_value"] = long_df["series_value"].astype(float)

    pivot_df = long_df.pivot(
        index="timestamps", columns="series_name", values="series_value"
    )

    pivot_df.to_csv(
        os.path.join(
            "data", "processed", str(args.n_samples), "web_traffic_expanded.csv"
        )
    )

    pivot_df.info()


if __name__ == "__main__":
    main()
