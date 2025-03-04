"""Auto-generated __init__.py for the droid group."""

__all__ = [
    "droid_splain",
    "man_splain",
]

from . import droid_splain
from . import man_splain


def run_group():
    """Entry point for running the droid command group directly."""
    import sys
    from starshipagentic.cli import main as cli_main
    sys.argv = ['starshipagentic', 'droid'] + sys.argv[1:]
    cli_main()
