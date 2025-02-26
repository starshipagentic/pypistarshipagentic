"""Mission commands for defining and expanding project requirements."""

import click
import sys
from rich.console import Console

console = Console()

@click.group(name="mission")
def mission_group():
    """Define and expand project requirements."""
    pass

@mission_group.command(name="mission-brief")
@click.argument("idea", required=True)
@click.option("--detailed", is_flag=True, help="Generate detailed documentation")
def mission_brief(idea, detailed):
    """Generate initial project documentation."""
    console.print("[bold]Generating mission brief...[/bold]")
    console.print(f"Project idea: {idea}")
    
    if detailed:
        console.print("Generating detailed documentation...")
    
    console.print("[green]Mission brief generated![/green]")

@mission_group.command(name="expand-mission")
@click.option("--focus", help="Area to expand upon")
def expand_mission(focus):
    """Elaborate on project requirements."""
    console.print("[bold]Expanding mission details...[/bold]")
    
    if focus:
        console.print(f"Focusing on: {focus}")
    
    console.print("[green]Mission expanded successfully![/green]")

# Command entry points for direct invocation
def mission_brief_command():
    """Entry point for the 'mission' command."""
    return mission_brief(sys.argv[1:])

def expand_mission_command():
    """Entry point for the 'expand' command."""
    return expand_mission(sys.argv[1:])
