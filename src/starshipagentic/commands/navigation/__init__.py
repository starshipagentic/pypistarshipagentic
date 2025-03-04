"""Auto-generated __init__.py for the navigation group."""

__all__ = [
    "plot_navigation",
    "set_waypoints",
]

from . import plot_navigation
from . import set_waypoints


def run_group():
    """Entry point for running the navigation command group directly."""
    import sys
    from starshipagentic.cli import main as cli_main
    sys.argv = ['starshipagentic', 'navigation'] + sys.argv[1:]
    cli_main()
