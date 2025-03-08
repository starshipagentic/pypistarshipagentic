"""Auto-generated __init__.py for the fleet_commander group."""

import click
fleet_commander_group = click.Group(name="fleet_commander")

__all__ = [
    "commission_ship",
    "tour_ship",
    "visualize_ship",
    "fleet_commander_group"
]

from . import commission_ship
from . import tour_ship
from . import visualize_ship


def run_group():
    """Entry point for running the fleet_commander command group directly."""
    import sys
    from starshipagentic.cli import main as cli_main
    original_args = sys.argv.copy()
    
    # When run as a standalone command (e.g., 'fleet_commander visualize-ship')
    # we need to transform it to 'starshipagentic fleet_commander visualize-ship'
    if len(original_args) > 1:
        # The command name is in original_args[0], subcommands start at index 1
        subcommands = original_args[1:]
        
        # Preserve all arguments after the command name
        sys.argv = ['starshipagentic', 'fleet_commander'] + subcommands
    else:
        # No subcommands, just show the group help
        sys.argv = ['starshipagentic', 'fleet_commander']
    
    cli_main()
