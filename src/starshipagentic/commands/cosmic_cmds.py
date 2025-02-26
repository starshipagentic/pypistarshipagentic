"""Cosmic commands for special operations."""

import click
import sys
from rich.console import Console

console = Console()

@click.group(name="cosmic")
def cosmic_group():
    """Special operations."""
    pass

@cosmic_group.command(name="supernova")
@click.option("--force", is_flag=True, help="Force removal without confirmation")
def supernova(force):
    """Clean up Git repositories and metadata."""
    if not force:
        console.print("[bold red]WARNING: This will remove all Git repositories and metadata.[/bold red]")
        console.print("Use --force to skip this warning.")
        return
    
    console.print("[bold]Initiating supernova sequence...[/bold]")
    console.print("[green]Git repositories and metadata removed![/green]")

# Command entry points for direct invocation
def supernova_command():
    """Entry point for the 'supernova' command."""
    return supernova(sys.argv[1:])
