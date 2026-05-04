from __future__ import annotations

from pathlib import Path

import pandas as pd
from openpyxl import load_workbook

from excel_automation_toolkit.pipeline import PipelineConfig, run_pipeline
from excel_automation_toolkit.preprocessing import clean_dataframe


def test_clean_dataframe_normalizes_headers_and_trims_text() -> None:
    df = pd.DataFrame(
        {
            " Order Date ": ["2026-01-01"],
            " Region ": [" North "],
            "Revenue": ["1,250"],
        }
    )

    cleaned = clean_dataframe(df, required_columns=["order_date"], date_columns=["order_date"])

    assert list(cleaned.columns) == ["order_date", "region", "revenue"]
    assert cleaned.loc[0, "region"] == "North"
    assert pd.Timestamp("2026-01-01") == cleaned.loc[0, "order_date"]


def test_pipeline_generates_formatted_workbook(tmp_path: Path) -> None:
    input_path = tmp_path / "sales.csv"
    output_path = tmp_path / "report.xlsx"
    input_path.write_text(
        "Order Date,Region,Revenue\n"
        "2026-01-01,North,100\n"
        "2026-01-02,North,250\n"
        "2026-01-03,South,75\n",
        encoding="utf-8",
    )

    result = run_pipeline(
        PipelineConfig(
            input_path=input_path,
            output_path=output_path,
            date_columns=("Order Date",),
            numeric_columns=("Revenue",),
            dimensions=("Region",),
            amount_column="Revenue",
        )
    )

    assert result == output_path
    workbook = load_workbook(output_path, read_only=False)
    assert {"Raw Data", "Processed Data", "Summary", "Metadata"} <= set(workbook.sheetnames)

    summary = workbook["Summary"]
    rows = list(summary.iter_rows(values_only=True))
    assert rows[0] == ("region", "revenue_count", "revenue_sum", "revenue_mean")
    assert ("North", 2, 350, 175) in rows

