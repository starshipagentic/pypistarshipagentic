"""Auto-generated __init__.py for the weapons group."""

__all__ = [
    "aim_lasers",
    "fire_photons",
    "shields_up",
]

from . import aim_lasers
from . import fire_photons
from . import shields_up


def run_group():
    """Entry point for running the weapons command group directly."""
    import sys
    from starshipagentic.cli import main as cli_main
    sys.argv = ['starshipagentic', 'weapons'] + sys.argv[1:]
    cli_main()
