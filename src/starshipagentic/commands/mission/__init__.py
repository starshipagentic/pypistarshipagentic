"""Auto-generated __init__.py for the mission group."""

__all__ = [
    "expand_mission",
    "mission_brief",
]

from . import expand_mission
from . import mission_brief


def run_group():
    """Entry point for running the mission command group directly."""
    import sys
    from starshipagentic.cli import main as cli_main
    sys.argv = ['starshipagentic', 'mission'] + sys.argv[1:]
    cli_main()
