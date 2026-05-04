from __future__ import annotations

import re
from collections.abc import Iterable

import pandas as pd


def normalize_column_name(name: object) -> str:
    """Convert Excel-friendly headers into stable snake_case column names."""
    value = str(name).strip().lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return re.sub(r"_+", "_", value).strip("_")


def clean_dataframe(
    df: pd.DataFrame,
    *,
    required_columns: Iterable[str] = (),
    date_columns: Iterable[str] = (),
    drop_duplicates: bool = True,
) -> pd.DataFrame:
    """Standardize headers, trim strings, remove empty rows, and parse date columns."""
    cleaned = df.copy()
    cleaned.columns = [normalize_column_name(column) for column in cleaned.columns]

    required = [normalize_column_name(column) for column in required_columns]
    missing = [column for column in required if column not in cleaned.columns]
    if missing:
        raise ValueError(f"Missing required columns after normalization: {', '.join(missing)}")

    text_columns = cleaned.select_dtypes(include=["object", "string"]).columns
    for column in text_columns:
        cleaned[column] = cleaned[column].map(lambda value: value.strip() if isinstance(value, str) else value)
        cleaned[column] = cleaned[column].replace("", pd.NA)

    cleaned = cleaned.dropna(how="all")
    if drop_duplicates:
        cleaned = cleaned.drop_duplicates()

    for column in date_columns:
        normalized = normalize_column_name(column)
        if normalized in cleaned.columns:
            cleaned[normalized] = pd.to_datetime(cleaned[normalized], errors="coerce")

    return cleaned.reset_index(drop=True)


def coerce_numeric_columns(df: pd.DataFrame, columns: Iterable[str]) -> pd.DataFrame:
    """Convert selected columns to numeric values while tolerating currency formatting."""
    coerced = df.copy()
    for column in columns:
        normalized = normalize_column_name(column)
        if normalized not in coerced.columns:
            continue
        series = coerced[normalized]
        if series.dtype == "object":
            series = series.astype(str).str.replace(r"[$,]", "", regex=True)
        coerced[normalized] = pd.to_numeric(series, errors="coerce")
    return coerced

