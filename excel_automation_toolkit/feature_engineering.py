from __future__ import annotations

from collections.abc import Iterable, Mapping

import pandas as pd

from .preprocessing import normalize_column_name


def add_time_features(df: pd.DataFrame, date_columns: Iterable[str]) -> pd.DataFrame:
    """Add year, quarter, month, and month_start columns for parsed date fields."""
    enriched = df.copy()
    for column in date_columns:
        normalized = normalize_column_name(column)
        if normalized not in enriched.columns:
            continue

        dates = pd.to_datetime(enriched[normalized], errors="coerce")
        enriched[f"{normalized}_year"] = dates.dt.year
        enriched[f"{normalized}_quarter"] = dates.dt.to_period("Q").astype("string")
        enriched[f"{normalized}_month"] = dates.dt.month
        enriched[f"{normalized}_month_start"] = dates.dt.to_period("M").dt.to_timestamp()
    return enriched


def aggregate_metrics(
    df: pd.DataFrame,
    *,
    dimensions: Iterable[str],
    metrics: Mapping[str, str | list[str]],
) -> pd.DataFrame:
    """Aggregate metrics by one or more business dimensions."""
    normalized_dimensions = [normalize_column_name(column) for column in dimensions]
    normalized_metrics = {
        normalize_column_name(column): functions for column, functions in metrics.items()
    }

    missing_dimensions = [column for column in normalized_dimensions if column not in df.columns]
    missing_metrics = [column for column in normalized_metrics if column not in df.columns]
    if missing_dimensions or missing_metrics:
        missing = ", ".join(missing_dimensions + missing_metrics)
        raise ValueError(f"Cannot aggregate because these columns are missing: {missing}")

    summary = df.groupby(normalized_dimensions, dropna=False).agg(normalized_metrics)
    summary.columns = [
        "_".join(part for part in column if part)
        if isinstance(column, tuple)
        else str(column)
        for column in summary.columns.to_flat_index()
    ]
    return summary.reset_index()

