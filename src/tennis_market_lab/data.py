"""Utilities for loading tennis market data."""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"


def load_csv(filename: str, *, processed: bool = False) -> pd.DataFrame:
    """Load a CSV file from the project's raw or processed data directory."""
    data_dir = PROCESSED_DATA_DIR if processed else RAW_DATA_DIR
    return pd.read_csv(data_dir / filename)
