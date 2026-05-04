from __future__ import annotations

import argparse
from pathlib import Path

from .pipeline import PipelineConfig, run_pipeline


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run an Excel automation pipeline.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run = subparsers.add_parser("run", help="Clean input data and generate an Excel report.")
    run.add_argument("--input", required=True, type=Path, help="CSV or Excel file to process.")
    run.add_argument(
        "--output",
        default=Path("data/processed/automation_report.xlsx"),
        type=Path,
        help="Destination .xlsx report path.",
    )
    run.add_argument("--sheet-name", default=0, help="Excel sheet name or index for workbook inputs.")
    run.add_argument("--required-column", action="append", default=[], help="Column that must exist.")
    run.add_argument("--date-column", action="append", default=[], help="Column to parse as a date.")
    run.add_argument("--numeric-column", action="append", default=[], help="Column to coerce to numeric.")
    run.add_argument("--dimension", action="append", default=[], help="Summary grouping dimension.")
    run.add_argument("--amount-column", help="Metric column for count, sum, and mean summaries.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "run":
        config = PipelineConfig(
            input_path=args.input,
            output_path=args.output,
            sheet_name=_parse_sheet_name(args.sheet_name),
            required_columns=tuple(args.required_column),
            date_columns=tuple(args.date_column),
            numeric_columns=tuple(args.numeric_column),
            dimensions=tuple(args.dimension),
            amount_column=args.amount_column,
        )
        report_path = run_pipeline(config)
        print(f"Report generated: {report_path}")
        return 0

    raise ValueError(f"Unsupported command: {args.command}")


def _parse_sheet_name(value: str) -> str | int:
    try:
        return int(value)
    except ValueError:
        return value


if __name__ == "__main__":
    raise SystemExit(main())

