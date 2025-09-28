import argparse
from cProfile import label
import os

from bokeh.plotting import show
import holoviews as hv
from holoviews.operation.datashader import (
    datashade,
    dynspread,
    rasterize,
    shade,
    spread,
)
import pandas as pd
import panel as pn

hv.extension("bokeh")
pn.extension()


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

    df = pd.read_csv(
        os.path.join(
            "data", "processed", str(args.n_samples), "web_traffic_expanded.csv"
        ),
        index_col="timestamps",
        parse_dates=True,
    )

    dates = df.index
    curve = hv.Curve((dates, df.iloc[:, 0]), label=df.columns[0])
    curve.opts(
        line_width=1,
        tools=["xwheel_zoom"],
        line_alpha=0.8,
        hover_tooltips=[
            ("Series", "$label"),
            ("Time", "$x{%F %T}"),
            ("Value", "$y{0.00}"),
        ],
        hover_formatters={"$x": "datetime"},
    )
    bokeh_plot = hv.render(curve, backend="bokeh")
    bokeh_plot.sizing_mode = "stretch_both"
    show(bokeh_plot)

    # rasterize(curve, width=800, line_width=3, pixel_ratio=2).opts(width=800, cmap=['lightblue','blue'])


if __name__ == "__main__":
    main()
