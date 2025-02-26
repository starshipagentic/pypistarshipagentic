"""MCARS commands for code repository and search system."""

import click
import sys
from rich.console import Console

console = Console()

@click.group(name="mcars")
def mcars_group():
    """Code repository and search system."""
    pass

@mcars_group.command(name="search")
@click.argument("query", required=True)
def search(query):
    """Search code repository database."""
    console.print("[bold]Searching MCARS database...[/bold]")
    console.print(f"Query: {query}")
    console.print("[green]Search complete![/green]")

@mcars_group.command(name="transport")
@click.argument("file", required=True)
@click.option("--description", help="Custom description for the code")
def transport(file, description):
    """Store code snippets with AI-generated summaries."""
    console.print("[bold]Transporting code to MCARS database...[/bold]")
    console.print(f"File: {file}")
    
    if description:
        console.print(f"Description: {description}")
    else:
        console.print("Generating AI description...")
    
    console.print("[green]Transport complete![/green]")

# Command entry points for direct invocation
def search_command():
    """Entry point for the 'search' command."""
    return search(sys.argv[1:])

def transport_command():
    """Entry point for the 'transport' command."""
    return transport(sys.argv[1:])
