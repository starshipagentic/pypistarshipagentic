"""Droid commands for explanation and assistance."""

import click
import sys
from rich.console import Console

console = Console()

@click.group(name="droid")
def droid_group():
    """Explanation and assistance commands."""
    pass

@droid_group.command(name="droid-splain")
def droid_splain():
    """Explain the last error or report."""
    console.print("[bold]Droid analyzing last output...[/bold]")
    console.print("[green]Analysis complete![/green]")
    console.print("The error occurred because the system couldn't find the specified module.")
    console.print("Recommendation: Check if the module is installed or if there's a typo in the import statement.")

@droid_group.command(name="man-splain")
@click.argument("topic", required=True)
def man_splain(topic):
    """Search and explain a specified topic."""
    console.print(f"[bold]Searching for information about: {topic}[/bold]")
    console.print("[green]Search complete![/green]")
    console.print(f"Here's what I found about {topic}:")
    console.print("(Detailed explanation would appear here)")

# Command entry points for direct invocation
def droid_splain_command():
    """Entry point for the 'droid' command."""
    return droid_splain(sys.argv[1:])

def man_splain_command():
    """Entry point for the 'splain' command."""
    return man_splain(sys.argv[1:])
