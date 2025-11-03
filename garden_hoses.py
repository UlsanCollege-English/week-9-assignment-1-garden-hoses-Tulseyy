"""Top-level compatibility shim for tests.

The tests load `garden_hoses.py` from the project root. The real
implementation is in `src/garden_hoses.py`, so import and re-export
the required symbol here to keep a single source of truth.
"""
from src.garden_hoses import min_cost_connect

__all__ = ["min_cost_connect"]
