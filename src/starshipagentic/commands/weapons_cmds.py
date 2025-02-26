"""Weapons commands for removing problematic code and tests."""

import click
import sys
from rich.console import Console

console = Console()

@click.group(name="weapons")
def weapons_group():
    """Remove problematic code and tests."""
    pass

@weapons_group.command(name="fire-photons")
@click.argument("target", required=True)
def fire_photons(target):
    """Remove problematic test steps."""
    console.print("[bold]Firing photon torpedoes...[/bold]")
    console.print(f"Target: {target}")
    console.print("[green]Target eliminated![/green]")

@weapons_group.command(name="aim-lasers")
@click.argument("target", required=True)
@click.option("--precision", type=int, default=3, help="Precision level (1-5)")
def aim_lasers(target, precision):
    """Remove problematic code sections."""
    console.print(f"[bold]Aiming lasers at {target} with precision level {precision}...[/bold]")
    console.print("[green]Target neutralized![/green]")

@weapons_group.command(name="shields-up")
@click.option("--level", type=int, default=100, help="Shield strength (0-100)")
def shields_up(level):
    """Activate defensive operations."""
    console.print(f"[bold]Raising shields to {level}%...[/bold]")
    console.print("[green]Shields activated![/green]")

# Command entry points for direct invocation
def fire_photons_command():
    """Entry point for the 'photons' command."""
    return fire_photons(sys.argv[1:])

def aim_lasers_command():
    """Entry point for the 'lasers' command."""
    return aim_lasers(sys.argv[1:])

def shields_up_command():
    """Entry point for the 'shields' command."""
    return shields_up(sys.argv[1:])
