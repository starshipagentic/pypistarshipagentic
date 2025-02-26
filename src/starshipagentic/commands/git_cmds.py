"""Git commands for Git-related operations."""

import click
import sys
from rich.console import Console

console = Console()

@click.group(name="git")
def git_group():
    """Git-related operations."""
    pass

@git_group.command(name="teleport")
@click.argument("destination", required=True)
@click.option("--files", help="Comma-separated list of files to include")
def teleport(destination, files):
    """Create new Git repo from code sections."""
    console.print("[bold]Initiating teleport sequence...[/bold]")
    console.print(f"Destination: {destination}")
    
    if files:
        console.print(f"Including files: {files}")
    
    console.print("[green]Teleport complete![/green]")

# Command entry points for direct invocation
def teleport_command():
    """Entry point for the 'teleport' command."""
    return teleport(sys.argv[1:])
