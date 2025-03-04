"""Auto-generated __init__.py for the architecture group."""

__all__ = [
    "calibrate_technology",
    "review_schematics",
]

from . import calibrate_technology
from . import review_schematics


def run_group():
    """Entry point for running the architecture command group directly."""
    import sys
    from starshipagentic.cli import main as cli_main
    sys.argv = ['starshipagentic', 'architecture'] + sys.argv[1:]
    cli_main()
