from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from .report_generator import build_report


@dataclass(frozen=True)
class PipelineConfig:
    input_path: Path
    output_path: Path = Path("data/processed/automation_report.xlsx")
    sheet_name: str | int | None = 0
    required_columns: tuple[str, ...] = field(default_factory=tuple)
    date_columns: tuple[str, ...] = field(default_factory=tuple)
    numeric_columns: tuple[str, ...] = field(default_factory=tuple)
    dimensions: tuple[str, ...] = field(default_factory=tuple)
    amount_column: str | None = None


def run_pipeline(config: PipelineConfig) -> Path:
    """Run the default load-clean-enrich-report workflow."""
    return build_report(
        config.input_path,
        config.output_path,
        sheet_name=config.sheet_name,
        required_columns=config.required_columns,
        date_columns=config.date_columns,
        numeric_columns=config.numeric_columns,
        dimensions=config.dimensions,
        amount_column=config.amount_column,
    )

