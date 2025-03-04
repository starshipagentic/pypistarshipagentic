import click
from .services import visualize_ship_service

@click.command()
@click.argument("input", required=False)
def visualize_ship_command(input=None):
    """
    Auto-generated CLI command for visualize_ship.
    """
    result = visualize_ship_service(input)
    click.echo(result)

if __name__ == "__main__":
    visualize_ship_command()
