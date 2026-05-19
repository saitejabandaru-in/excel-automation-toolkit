"""Excel Automation Toolkit public API."""

from importlib.metadata import PackageNotFoundError, version

from .pipeline import PipelineConfig, run_pipeline
from .report_generator import build_report

try:
    __version__ = version("excel-automation-toolkit")
except PackageNotFoundError:
    __version__ = "0.1.0"

__all__ = ["PipelineConfig", "__version__", "build_report", "run_pipeline"]
