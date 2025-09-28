import argparse
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
    curves = []
    for i, (series_name, series_data) in enumerate(df.items()):
        curve = hv.Curve((dates, series_data), label=series_name)
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
        curves.append(curve)

    curves_overlay = hv.Overlay(curves).opts(
        title="Web Traffic Data",
        xlabel="Time",
        ylabel="Number of Requests",
        responsive=True,
        show_legend=True,
    )

    bokeh_plot = hv.render(curves_overlay, backend="bokeh")
    bokeh_plot.sizing_mode = "stretch_both"
    show(bokeh_plot)


if __name__ == "__main__":
    main()
