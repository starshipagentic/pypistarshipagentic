"""Auto-generated __init__.py for the probe group."""

__all__ = [
    "build_landing_zone",
    "fabricate_infrastructure",
    "map_planet",
]

from . import build_landing_zone
from . import fabricate_infrastructure
from . import map_planet


def run_group():
    """Entry point for running the probe command group directly."""
    import sys
    from starshipagentic.cli import main as cli_main
    sys.argv = ['starshipagentic', 'probe'] + sys.argv[1:]
    cli_main()
