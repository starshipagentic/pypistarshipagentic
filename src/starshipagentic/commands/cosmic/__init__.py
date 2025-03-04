"""Auto-generated __init__.py for the cosmic group."""

__all__ = [
    "supernova",
]

from . import supernova


def run_group():
    """Entry point for running the cosmic command group directly."""
    import sys
    from starshipagentic.cli import main as cli_main
    sys.argv = ['starshipagentic', 'cosmic'] + sys.argv[1:]
    cli_main()
