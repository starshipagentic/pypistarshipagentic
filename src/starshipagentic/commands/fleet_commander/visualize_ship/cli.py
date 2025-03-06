import click
from starshipagentic.visualization.pygame_display import display_ship_visualization

@click.command()
@click.option('--ship', default='scout', help='Ship to visualize (scout, enterprise, voyager, defiant, django, flask, react)')
def visualize_ship_command(ship=None):
    """Launch a Pygame visualization of the specified ship."""
    if not ship:
        ship = 'scout'  # Default ship
    
    # Launch the pygame visualization
    display_ship_visualization(ship)
    
    return f"Visualization of {ship} completed."

if __name__ == "__main__":
    visualize_ship_command()
