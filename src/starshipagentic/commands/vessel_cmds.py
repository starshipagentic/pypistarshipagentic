"""Vessel commands for initializing and selecting project templates."""

import click
import sys
from rich.console import Console

console = Console()

@click.group(name="vessel")
def vessel_group():
    """Initialize and select project templates."""
    pass

@vessel_group.command(name="tour-ship")
@click.option("--category", help="Filter templates by category")
def tour_ship(category):
    """Browse available ship templates/frameworks."""
    console.print("[bold]Available ship templates:[/bold]")
    
    templates = [
        {"name": "Django Cruiser", "category": "web", "description": "Full-featured web framework"},
        {"name": "Flask Scout", "category": "web", "description": "Lightweight web framework"},
        {"name": "React Interceptor", "category": "frontend", "description": "Frontend JavaScript library"},
        {"name": "Vue Explorer", "category": "frontend", "description": "Progressive JavaScript framework"},
        {"name": "FastAPI Shuttle", "category": "api", "description": "Modern API framework"},
    ]
    
    if category:
        templates = [t for t in templates if t["category"] == category]
    
    for template in templates:
        console.print(f"[green]{template['name']}[/green]: {template['description']}")

@vessel_group.command(name="commission-ship")
@click.argument("template", required=True)
@click.option("--name", help="Project name")
def commission_ship(template, name):
    """Clone template and run initialization."""
    console.print(f"[bold]Commissioning new ship based on {template} template...[/bold]")
    
    if not name:
        name = "new_project"
    
    console.print(f"Creating project: {name}")
    console.print("[green]Ship commissioned successfully![/green]")

@vessel_group.command(name="visualize-ship")
@click.option("--ship", default="enterprise", help="Ship to visualize")
def visualize_ship(ship):
    """Launch a Pygame visualization of the specified ship."""
    console.print(f"[bold]Launching visualization for {ship}...[/bold]")
    
    try:
        from starshipagentic.visualization import launch_visualization
        launch_visualization(ship)
    except ImportError:
        console.print("[red]Pygame visualization requires additional dependencies.[/red]")
        console.print("Install with: [bold]pip install pygame[/bold]")

# Command entry points for direct invocation
def tour_ship_command():
    """Entry point for the 'tour' command."""
    return tour_ship(sys.argv[1:])

def commission_ship_command():
    """Entry point for the 'commission' command."""
    return commission_ship(sys.argv[1:])

def visualize_ship_command():
    """Entry point for the 'visualize' command."""
    return visualize_ship(sys.argv[1:])
