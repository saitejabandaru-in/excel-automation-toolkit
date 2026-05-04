from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd

SUPPORTED_EXTENSIONS = {".csv", ".xlsx", ".xlsm", ".xls"}


def load_table(path: str | Path, sheet_name: str | int | None = 0) -> pd.DataFrame:
    """Load a CSV or Excel worksheet into a dataframe."""
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Input file does not exist: {file_path}")

    suffix = file_path.suffix.lower()
    if suffix == ".csv":
        return pd.read_csv(file_path)
    if suffix in {".xlsx", ".xlsm", ".xls"}:
        return pd.read_excel(file_path, sheet_name=sheet_name)

    supported = ", ".join(sorted(SUPPORTED_EXTENSIONS))
    raise ValueError(f"Unsupported input type '{suffix}'. Supported types: {supported}")


def load_many(paths: Iterable[str | Path], sheet_name: str | int | None = 0) -> pd.DataFrame:
    """Load and concatenate multiple source files, tagging each row with its source file."""
    frames: list[pd.DataFrame] = []
    for path in paths:
        file_path = Path(path)
        frame = load_table(file_path, sheet_name=sheet_name)
        frame.insert(0, "source_file", file_path.name)
        frames.append(frame)

    if not frames:
        raise ValueError("No input files were provided")
    return pd.concat(frames, ignore_index=True)


def find_input_files(directory: str | Path) -> list[Path]:
    """Return supported input files in a directory sorted by filename."""
    root = Path(directory)
    if not root.exists():
        raise FileNotFoundError(f"Input directory does not exist: {root}")
    if not root.is_dir():
        raise NotADirectoryError(f"Input path is not a directory: {root}")

    return sorted(
        path
        for path in root.iterdir()
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS
    )


def validate_columns(df: pd.DataFrame, required_columns: Iterable[str]) -> None:
    """Raise a clear error when expected columns are missing."""
    missing = [column for column in required_columns if column not in df.columns]
    if missing:
        available = ", ".join(map(str, df.columns))
        expected = ", ".join(missing)
        raise ValueError(f"Missing required columns: {expected}. Available columns: {available}")

