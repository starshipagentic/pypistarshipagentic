"""Auto-generated __init__.py for the beam group."""

__all__ = [
    "teleport",
]

from . import teleport


def run_group():
    """Entry point for running the beam command group directly."""
    import sys
    from starshipagentic.cli import main as cli_main
    sys.argv = ['starshipagentic', 'beam'] + sys.argv[1:]
    cli_main()
