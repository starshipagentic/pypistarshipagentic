"""Auto-generated __init__.py for the vessel group."""

__all__ = [
    "commission_ship",
    "tour_ship",
    "visualize_ship",
]

from . import commission_ship
from . import tour_ship
from . import visualize_ship


def run_group():
    """Entry point for running the vessel command group directly."""
    import sys
    from starshipagentic.cli import main as cli_main
    sys.argv = ['starshipagentic', 'vessel'] + sys.argv[1:]
    cli_main()
