"""Commands for generating initial code tracks and connecting BDD step coverage."""

import click
from rich.console import Console
from starshipagentic.utils.base_command import BaseCommand
from starshipagentic.utils.interactive import prompt_for_missing_param

console = Console()

# Create the command group
send_probe_group = click.Group(
    name="send-probe",
    help="Generate initial code tracks and connect the top down BDD step coverage"
)

@send_probe_group.command(name="map-planet")
@click.option("--feature", help="Feature to map planet for")
def map_planet(feature):
    """Lightweight: create initial folder, and file names scaffolding, not the BDD steps yet."""
    feature_name = BaseCommand.get_param_value(
        None, feature, "feature", "Enter feature name to map planet for"
    )
    
    click.echo(f"🌍 Mapping planet for feature: {feature_name}")
    click.echo("Creating initial folder and file structure...")
    # Implementation would go here
    click.echo("✅ Planet mapping complete!")

@send_probe_group.command(name="build-landing-zone")
@click.option("--feature", help="Feature to build landing zone for")
def build_landing_zone(feature):
    """Create initial code tracks within the files that map-planet created."""
    feature_name = BaseCommand.get_param_value(
        None, feature, "feature", "Enter feature name to build landing zone for"
    )
    
    click.echo(f"🚀 Building landing zone for feature: {feature_name}")
    click.echo("Creating initial code tracks...")
    # Implementation would go here
    click.echo("✅ Landing zone built successfully!")

@send_probe_group.command(name="fabricate-infrastructure")
@click.option("--feature", help="Feature to fabricate code for")
def fabricate_infrastructure(feature):
    """Generate BDD steps to connect the code laid down in the landing zone."""
    feature_name = BaseCommand.get_param_value(
        None, feature, "feature", "Enter feature name to fabricate infrastructure for"
    )
    
    click.echo(f"🏗️ Fabricating infrastructure for feature: {feature_name}")
    click.echo("Generating BDD steps...")
    # Implementation would go here
    click.echo("✅ Infrastructure fabrication complete!")

# Create command functions for direct invocation
def map_planet_command():
    """Wrapper for direct invocation of map_planet command."""
    BaseCommand.parse_args_for_command(map_planet)()

def build_landing_zone_command():
    """Wrapper for direct invocation of build_landing_zone command."""
    BaseCommand.parse_args_for_command(build_landing_zone)()

def fabricate_infrastructure_command():
    """Wrapper for direct invocation of fabricate_infrastructure command."""
    BaseCommand.parse_args_for_command(fabricate_infrastructure)()
