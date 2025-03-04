"""Auto-generated __init__.py for the transmission group."""

__all__ = [
    "authorize_codes",
    "receive_transmission",
    "scan_sector",
]

from . import authorize_codes
from . import receive_transmission
from . import scan_sector


def run_group():
    """Entry point for running the transmission command group directly."""
    import sys
    from starshipagentic.cli import main as cli_main
    sys.argv = ['starshipagentic', 'transmission'] + sys.argv[1:]
    cli_main()
