"""Visualization package for Starship Agentic."""

def launch_visualization(ship_name):
    """Launch the visualization interface for the specified ship."""
    try:
        from .pygame_display import display_ship_visualization
        display_ship_visualization(ship_name)
    except ImportError:
        raise ImportError("Pygame is required for visualization features")
