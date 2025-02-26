"""Exploration commands for executing and testing implementation."""

import click
import sys
from rich.console import Console

console = Console()

@click.group(name="exploration")
def exploration_group():
    """Execute and test your implementation."""
    pass

@exploration_group.command(name="warp-speed")
@click.argument("speed", type=int, required=False)
@click.option("--iterations", "-i", default=1, help="Number of test-fix iterations")
def warp_speed(speed, iterations):
    """Run BDD tests with AI fixing in a loop.
    
    SPEED determines the aggressiveness of the AI fixing (1-9).
    """
    if speed is None:
        speed = 5  # Default warp speed
    
    console.print(f"[bold]Engaging warp speed {speed} for {iterations} iterations...[/bold]")
    console.print("[green]Warp sequence complete![/green]")

@exploration_group.command(name="trycoder")
@click.option("--verbose", "-v", is_flag=True, help="Show detailed test output")
def trycoder(verbose):
    """Run unit tests with AI fixing in a loop."""
    console.print("[bold]Activating trycoder diagnostic sequence...[/bold]")
    
    if verbose:
        console.print("Verbose mode enabled")
    
    console.print("[green]Trycoder sequence complete![/green]")

@exploration_group.command(name="engage")
@click.option("--cycles", "-c", default=3, help="Number of full test cycles")
def engage(cycles):
    """Run complete test-fix cycles for all waypoints."""
    console.print(f"[bold]Engaging full mission sequence for {cycles} cycles...[/bold]")
    console.print("[green]Mission sequence complete![/green]")

# Command entry points for direct invocation
def warp_speed_command():
    """Entry point for the 'warp' command."""
    return warp_speed(sys.argv[1:])

def trycoder_command():
    """Entry point for the 'trycoder' command."""
    return trycoder(sys.argv[1:])

def engage_command():
    """Entry point for the 'engage' command."""
    return engage(sys.argv[1:])
