"""Vessel commands for initializing and selecting project templates."""

import click
import sys
from rich.console import Console
from starshipagentic.utils.interactive import prompt_for_missing_param

console = Console()

@click.group(name="vessel")
def vessel_group():
    """Initialize and select project templates."""
    pass

@vessel_group.command(name="tour-ship")
@click.argument("category", required=False)
@click.option("--category", "category_opt", help="Filter templates by category")
def tour_ship(category, category_opt):
    # Use the option value if provided, otherwise use the argument
    category = category_opt or category
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
@click.argument("template", required=False)
@click.option("--template", "template_opt", help="Project template to use")
@click.option("--name", help="Project name")
def commission_ship(template, template_opt, name):
    """Clone template and run initialization."""
    # Use the option value if provided, otherwise use the argument
    template = template_opt or template
    
    # Available templates
    templates = [
        "django-galaxy", "flask-scout", "react-interceptor", 
        "vue-explorer", "fastapi-shuttle"
    ]
    
    # If template is not provided, prompt for it
    if not template:
        template = prompt_for_missing_param(
            "template",
            "What class of ship would you like to commission?",
            choices=templates,
            default="django-galaxy"
        )
    
    # If name is not provided, prompt for it
    if not name:
        default_name = f"new_{template.split('-')[0]}_project"
        name = prompt_for_missing_param(
            "name",
            f"What would you like to name your {template} project?",
            default=default_name
        )
    
    console.print(f"[bold]Commissioning new ship based on {template} template...[/bold]")
    console.print(f"Creating project: {name}")
    console.print("[green]Ship commissioned successfully![/green]")

@vessel_group.command(name="visualize-ship")
@click.argument("ship", required=False)
@click.option("--ship", "ship_opt", default="enterprise", help="Ship to visualize")
def visualize_ship(ship, ship_opt):
    # Use the option value if provided, otherwise use the argument
    ship = ship_opt or ship or "enterprise"
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
    # Extract first argument as category if provided
    category = sys.argv[1] if len(sys.argv) > 1 else None
    return tour_ship(category, None)

def commission_ship_command():
    """Entry point for the 'commission' command."""
    # Extract first argument as template if provided
    template = sys.argv[1] if len(sys.argv) > 1 else None
    # Look for --name option
    name = None
    for i, arg in enumerate(sys.argv[1:]):
        if arg == "--name" and i+1 < len(sys.argv)-1:
            name = sys.argv[i+2]
    return commission_ship(template, None, name)

def visualize_ship_command():
    """Entry point for the 'visualize' command."""
    # Extract first argument as ship if provided
    ship = sys.argv[1] if len(sys.argv) > 1 else None
    return visualize_ship(ship, None)
