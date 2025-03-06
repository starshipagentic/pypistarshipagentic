import click
from starshipagentic.visualization.pygame_display import display_ship_visualization

@click.command()
@click.option('--ship', default='enterprise', help='Ship to visualize (enterprise, voyager, defiant, django, flask, react)')
def visualize_ship_command(ship=None):
    """Launch a Pygame visualization of the specified ship."""
    if not ship:
        ship = 'enterprise'  # Default ship
    
    # Launch the pygame visualization
    display_ship_visualization(ship)
    
    return f"Visualization of {ship} completed."

if __name__ == "__main__":
    visualize_ship_command()
