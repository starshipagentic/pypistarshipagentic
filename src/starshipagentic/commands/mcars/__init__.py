"""Auto-generated __init__.py for the mcars group."""

__all__ = [
    "search",
    "transport",
]

from . import search
from . import transport


def run_group():
    """Entry point for running the mcars command group directly."""
    import sys
    from starshipagentic.cli import main as cli_main
    sys.argv = ['starshipagentic', 'mcars'] + sys.argv[1:]
    cli_main()
