"""Architecture commands for reviewing and configuring system architecture."""

import click
import sys
from rich.console import Console

console = Console()

@click.group(name="architecture")
def architecture_group():
    """Review and configure system architecture."""
    pass

@architecture_group.command(name="review-schematics")
@click.option("--type", help="Type of diagram to review")
def review_schematics(type):
    """Review state diagrams and DDD docs."""
    console.print("[bold]Reviewing system schematics...[/bold]")
    
    if type:
        console.print(f"Focusing on {type} diagrams")
    else:
        console.print("Reviewing all system diagrams")
    
    console.print("[green]Schematics review complete![/green]")

@architecture_group.command(name="calibrate-technology")
@click.option("--stack", help="Technology stack to configure")
def calibrate_technology(stack):
    """Configure tech stack settings."""
    console.print("[bold]Calibrating technology stack...[/bold]")
    
    if stack:
        console.print(f"Configuring {stack} stack")
    else:
        console.print("Configuring default technology stack")
    
    console.print("[green]Technology calibration complete![/green]")

# Command entry points for direct invocation
def review_schematics_command():
    """Entry point for the 'schematics' command."""
    return review_schematics(sys.argv[1:])

def calibrate_technology_command():
    """Entry point for the 'calibrate' command."""
    return calibrate_technology(sys.argv[1:])
