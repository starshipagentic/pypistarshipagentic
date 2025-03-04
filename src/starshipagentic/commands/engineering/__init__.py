"""Auto-generated __init__.py for the engineering group."""

__all__ = [
    "complexity_report",
    "create_checkpoint",
    "inspect_vessel",
    "restore_checkpoint",
]

from . import complexity_report
from . import create_checkpoint
from . import inspect_vessel
from . import restore_checkpoint


def run_group():
    """Entry point for running the engineering command group directly."""
    import sys
    from starshipagentic.cli import main as cli_main
    sys.argv = ['starshipagentic', 'engineering'] + sys.argv[1:]
    cli_main()
