"""Excel Automation Toolkit public API."""

from .pipeline import PipelineConfig, run_pipeline
from .report_generator import build_report

__all__ = ["PipelineConfig", "build_report", "run_pipeline"]

