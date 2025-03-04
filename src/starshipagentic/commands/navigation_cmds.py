"""Navigation commands for planning feature implementation."""

import click
import sys
from rich.console import Console
from starshipagentic.utils.base_command import BaseCommand

console = Console()

@click.group(name="navigation")
def navigation_group():
    """Plan feature implementation."""
    pass

@navigation_group.command(name="plot-navigation")
@click.option("--format", help="Output format for features")
def plot_navigation(format):
    """Generate and review BDD Gherkin features."""
    console.print("[bold]Plotting navigation course...[/bold]")
    
    if format:
        console.print(f"Using {format} format for feature files")
    
    console.print("[green]Navigation course plotted![/green]")

@navigation_group.command(name="set-waypoints")
@click.option("--priority", help="Prioritization method")
def set_waypoints(priority):
    """Create prioritized feature implementation plan."""
    console.print("[bold]Setting development waypoints...[/bold]")
    
    if priority:
        console.print(f"Using {priority} prioritization method")
    
    console.print("[green]Waypoints established![/green]")

# Command entry points for direct invocation
def plot_navigation_command():
    """Entry point for the 'navigation' command."""
    BaseCommand.parse_args_for_command(plot_navigation)()

def set_waypoints_command():
    """Entry point for the 'waypoints' command."""
    BaseCommand.parse_args_for_command(set_waypoints)()
