"""Auto-generated __init__.py for the fleet_commander group."""

import click
fleet_commander_group = click.Group(name="fleet_commander")
# Add debugging override for fleet_commander_group.invoke
def debug_invoke(ctx):
    from rich.console import Console
    console = Console()
    console.print(f"[bold red]DEBUG: fleet_commander_group.invoke called, ctx.invoked_subcommand={ctx.invoked_subcommand}, ctx.args={ctx.args}[/bold red]")
    return fleet_commander_group.__orig_invoke__(ctx)
fleet_commander_group.__orig_invoke__ = fleet_commander_group.invoke
fleet_commander_group.invoke = debug_invoke

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
    from rich.console import Console
    console = Console()
    console.print("[bold red]DEBUG: run_group() called for fleet_commander[/bold red]")
    import sys
    from starshipagentic.cli import main as cli_main
    sys.argv = ['starshipagentic', 'fleet_commander']
    console.print("[bold red]DEBUG: run_group() invoking cli_main() for fleet_commander[/bold red]")
    cli_main()
