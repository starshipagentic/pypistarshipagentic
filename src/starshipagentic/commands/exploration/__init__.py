"""Auto-generated __init__.py for the exploration group."""

__all__ = [
    "engage",
    "trycoder",
    "warp_speed",
]

from . import engage
from . import trycoder
from . import warp_speed


def run_group():
    """Entry point for running the exploration command group directly."""
    import sys
    from starshipagentic.cli import main as cli_main
    sys.argv = ['starshipagentic', 'exploration'] + sys.argv[1:]
    cli_main()
