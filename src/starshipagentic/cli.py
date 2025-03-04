# [AUTO-GENERATED COMMAND IMPORTS START]
from starshipagentic.commands.vessel import run_group  # alias: vessel
from starshipagentic.commands.mission.mission_brief.cli import mission_brief_command  # alias: mission
from starshipagentic.commands.architecture import run_group  # alias: architecture
from starshipagentic.commands.navigation.plot_navigation.cli import plot_navigation_command  # alias: navigation
from starshipagentic.commands.transmission.receive_transmission.cli import receive_transmission_command  # alias: transmission
from starshipagentic.commands.probe import run_group  # alias: probe
from starshipagentic.commands.exploration import run_group  # alias: exploration
from starshipagentic.commands.weapons import run_group  # alias: weapons
from starshipagentic.commands.engineering import run_group  # alias: engineering
from starshipagentic.commands.cosmic import run_group  # alias: cosmic
from starshipagentic.commands.beam import run_group  # alias: beam
from starshipagentic.commands.mcars import run_group  # alias: mcars
from starshipagentic.commands.droid.droid_splain.cli import droid_splain_command  # alias: droid
from starshipagentic.commands.vessel.tour_ship.cli import tour_ship_command  # alias: tour-ship
from starshipagentic.commands.vessel.tour_ship.cli import tour_ship_command  # alias: tour
from starshipagentic.commands.vessel.commission_ship.cli import commission_ship_command  # alias: commission-ship
from starshipagentic.commands.vessel.commission_ship.cli import commission_ship_command  # alias: commission
from starshipagentic.commands.vessel.visualize_ship.cli import visualize_ship_command  # alias: visualize-ship
from starshipagentic.commands.mission.mission_brief.cli import mission_brief_command  # alias: mission-brief
from starshipagentic.commands.mission.expand_mission.cli import expand_mission_command  # alias: expand-mission
from starshipagentic.commands.mission.expand_mission.cli import expand_mission_command  # alias: expand
from starshipagentic.commands.architecture.review_schematics.cli import review_schematics_command  # alias: review-schematics
from starshipagentic.commands.architecture.review_schematics.cli import review_schematics_command  # alias: schematics
from starshipagentic.commands.architecture.calibrate_technology.cli import calibrate_technology_command  # alias: calibrate-technology
from starshipagentic.commands.architecture.calibrate_technology.cli import calibrate_technology_command  # alias: calibrate
from starshipagentic.commands.navigation.plot_navigation.cli import plot_navigation_command  # alias: plot-navigation
from starshipagentic.commands.navigation.set_waypoints.cli import set_waypoints_command  # alias: set-waypoints
from starshipagentic.commands.navigation.set_waypoints.cli import set_waypoints_command  # alias: waypoints
from starshipagentic.commands.transmission.authorize_codes.cli import authorize_codes_command  # alias: authorize-codes
from starshipagentic.commands.transmission.authorize_codes.cli import authorize_codes_command  # alias: authorize
from starshipagentic.commands.transmission.scan_sector.cli import scan_sector_command  # alias: scan-sector
from starshipagentic.commands.transmission.scan_sector.cli import scan_sector_command  # alias: scan
from starshipagentic.commands.transmission.receive_transmission.cli import receive_transmission_command  # alias: receive-transmission
from starshipagentic.commands.probe.map_planet.cli import map_planet_command  # alias: map-planet
from starshipagentic.commands.probe.map_planet.cli import map_planet_command  # alias: map
from starshipagentic.commands.probe.build_landing_zone.cli import build_landing_zone_command  # alias: build-landing-zone
from starshipagentic.commands.probe.build_landing_zone.cli import build_landing_zone_command  # alias: buildlz
from starshipagentic.commands.probe.fabricate_infrastructure.cli import fabricate_infrastructure_command  # alias: fabricate-infrastructure
from starshipagentic.commands.probe.fabricate_infrastructure.cli import fabricate_infrastructure_command  # alias: fabricate
from starshipagentic.commands.exploration.warp_speed.cli import warp_speed_command  # alias: warp-speed
from starshipagentic.commands.exploration.warp_speed.cli import warp_speed_command  # alias: warp
from starshipagentic.commands.exploration.trycoder.cli import trycoder_command  # alias: trycoder
from starshipagentic.commands.exploration.engage.cli import engage_command  # alias: engage
from starshipagentic.commands.weapons.fire_photons.cli import fire_photons_command  # alias: fire-photons
from starshipagentic.commands.weapons.fire_photons.cli import fire_photons_command  # alias: photons
from starshipagentic.commands.weapons.aim_lasers.cli import aim_lasers_command  # alias: aim-lasers
from starshipagentic.commands.weapons.aim_lasers.cli import aim_lasers_command  # alias: lasers
from starshipagentic.commands.weapons.shields_up.cli import shields_up_command  # alias: shields-up
from starshipagentic.commands.weapons.shields_up.cli import shields_up_command  # alias: shields
from starshipagentic.commands.engineering.create_checkpoint.cli import create_checkpoint_command  # alias: create-checkpoint
from starshipagentic.commands.engineering.create_checkpoint.cli import create_checkpoint_command  # alias: checkpoint
from starshipagentic.commands.engineering.restore_checkpoint.cli import restore_checkpoint_command  # alias: restore-checkpoint
from starshipagentic.commands.engineering.restore_checkpoint.cli import restore_checkpoint_command  # alias: restore
from starshipagentic.commands.engineering.inspect_vessel.cli import inspect_vessel_command  # alias: inspect-vessel
from starshipagentic.commands.engineering.inspect_vessel.cli import inspect_vessel_command  # alias: inspect
from starshipagentic.commands.engineering.complexity_report.cli import complexity_report_command  # alias: complexity-report
from starshipagentic.commands.engineering.complexity_report.cli import complexity_report_command  # alias: complexity
from starshipagentic.commands.cosmic.supernova.cli import supernova_command  # alias: supernova
from starshipagentic.commands.beam.teleport.cli import teleport_command  # alias: teleport
from starshipagentic.commands.mcars.search.cli import search_command  # alias: search
from starshipagentic.commands.mcars.transport.cli import transport_command  # alias: transport
from starshipagentic.commands.droid.droid_splain.cli import droid_splain_command  # alias: droid-splain
from starshipagentic.commands.droid.man_splain.cli import man_splain_command  # alias: man-splain
from starshipagentic.commands.droid.man_splain.cli import man_splain_command  # alias: splain
# [AUTO-GENERATED COMMAND IMPORTS END]
# Starship Agentic License Header
#
# Copyright (c) 2025 Travis Somerville and David Samson
#
# This file is part of Starship Agentic.
#
# It is licensed under the GNU Affero General Public License (AGPL) v3 or later.
# For full details, see the LICENSE.md file in the project root.
"""Main CLI entry point for Starship Agentic."""

import click
import sys
import yaml
import os
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.markdown import Markdown
from functools import update_wrapper

# Import command registry
from starshipagentic.utils.command_registry import command_registry

# Import command groups
from starshipagentic.commands import (
    architecture,
    beam,
    cosmic,
    droid,
    engineering,
    exploration,
    mcars,
    mission,
    navigation,
    probe,
    transmission,
    vessel,
    weapons,
)

console = Console()

# Command group themes/colors for consistent styling
GROUP_THEMES = {
    "architecture": "magenta",
    "beam": "blue",
    "cosmic": "bright_magenta",
    "droid": "bright_white",
    "engineering": "bright_green",
    "exploration": "bright_blue",
    "mcars": "bright_yellow",
    "mission": "green",
    "navigation": "cyan",
    "probe": "blue",
    "transmission": "yellow",
    "vessel": "blue",
    "weapons": "red",
}

# Command group icons
GROUP_ICONS = {
    "architecture": "🏗️",
    "beam": "🚀",
    "cosmic": "✨",
    "droid": "🤖",
    "engineering": "🔧",
    "exploration": "🔭",
    "mcars": "🔍",
    "mission": "📋",
    "navigation": "🧭",
    "probe": "🚀",
    "transmission": "📡",
    "vessel": "🚢",
    "weapons": "🛡️",
}

def display_welcome():
    """Display welcome message with ASCII art."""
    welcome_text = """
    ███████╗████████╗ █████╗ ██████╗ ███████╗██╗  ██╗██╗██████╗ 
    ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║  ██║██║██╔══██╗
    ███████╗   ██║   ███████║██████╔╝███████╗███████║██║██████╔╝
    ╚════██║   ██║   ██╔══██║██╔══██╗╚════██║██╔══██║██║██╔═══╝ 
    ███████║   ██║   ██║  ██║██║  ██║███████║██║  ██║██║██║     
    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     
    
     █████╗  ██████╗ ███████╗███╗   ██╗████████╗██╗ ██████╗
    ██╔══██╗██╔════╝ ██╔════╝████╗  ██║╚══██╔══╝██║██╔════╝
    ███████║██║  ███╗█████╗  ██╔██╗ ██║   ██║   ██║██║     
    ██╔══██║██║   ██║██╔══╝  ██║╚██╗██║   ██║   ██║██║     
    ██║  ██║╚██████╔╝███████╗██║ ╚████║   ██║   ██║╚██████╗
    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝ ╚═════╝
    """
    
    console.print(Panel(Text(welcome_text, style="bold blue")))
    console.print("Welcome to Starship Agentic - AI-assisted software development with a Star Trek-inspired interface.")

def enhance_group_help(group, name):
    """Enhance a command group's help display."""
    original_format_help = group.format_help
    
    def enhanced_format_help(ctx, formatter):
        # Use rich to display a better help
        theme_color = GROUP_THEMES.get(name, "white")
        icon = GROUP_ICONS.get(name, "🚀")
        
        # Get group info from registry
        group_info = command_registry.get_group_info(name)
        
        # Group header with icon and styled name
        header = f"{icon} {name.upper()} COMMANDS"
        console.print(Panel(header, style=f"bold {theme_color}"))
        
        # Group description - use registry description if available, otherwise use Click group help
        description = group_info.get('description') or group.help or "No description"
        console.print(Markdown(f"**Description:** {description}"))
        console.print("")
        
        # Commands table
        table = Table(show_header=True, header_style=f"bold {theme_color}")
        table.add_column("Command", style=f"{theme_color}")
        table.add_column("Aliases", style="yellow")
        table.add_column("Description", style="white")
        table.add_column("Options", style="dim")
        
        # Add commands to table
        for cmd_name in sorted(group.commands):
            cmd = group.commands[cmd_name]
            
            # Get command info from registry
            cmd_info = command_registry.get_command_info(name, cmd_name)
            
            # Get options from Click command
            options = []
            for param in cmd.params:
                if isinstance(param, click.Option):
                    opt_str = f"--{param.name}"
                    if param.required:
                        opt_str += " (required)"
                    options.append(opt_str)
            
            # Get aliases from registry (which now uses pyproject.toml)
            aliases = command_registry.get_aliases_for_command(name, cmd_name)
            aliases_str = ", ".join(aliases) if aliases else "None"
            
            # Get description from registry or Click command
            description = cmd_info.get('description') or cmd.help or "No description"
            
            options_str = ", ".join(options) if options else "None"
            table.add_row(
                f"{name} {cmd_name}",
                aliases_str,
                description,
                options_str
            )
        
        console.print(table)
        console.print("")
        console.print(f"For more details on a specific command, type: [bold]starshipagentic {name} COMMAND --help[/bold]")
        
        # Skip the default Click help formatting
        return
    
    # Replace the format_help method
    group.format_help = enhanced_format_help
    update_wrapper(group.format_help, original_format_help)
    
    return group

def display_available_commands():
    """Display all available commands in a user-friendly format."""
    
    console.print(Panel("Available Command Categories", style="bold white"))
    
    # Create a table for command categories
    table = Table(show_header=True, header_style="bold")
    table.add_column("Category", style="cyan")
    table.add_column("Icon", style="yellow")
    table.add_column("Description", style="green")
    table.add_column("Example Command", style="bright_blue")
    
    # Add each command group with description and example from registry
    for group_name in command_registry.get_all_groups():
        group_info = command_registry.get_group_info(group_name)
        icon = GROUP_ICONS.get(group_name, "🚀")
        description = group_info.get('description', 'No description')
        example = command_registry.get_example_command(group_name)
        
        table.add_row(group_name, icon, description, example)
    
    console.print(table)
    
    console.print("\nTo see commands in a category: [bold]starshipagentic CATEGORY --help[/bold]")
    console.print("For details on a specific command: [bold]starshipagentic CATEGORY COMMAND --help[/bold]")

def display_all_commands():
    """Display all available commands in a detailed format."""
    
    console.print(Panel("All Available Commands", style="bold white"))
    
    # Create a table for all commands
    table = Table(show_header=True, header_style="bold")
    table.add_column("Command", style="cyan")
    table.add_column("Description", style="green")
    
    # Add commands from each group using the registry
    for group_name in command_registry.get_all_groups():
        group_info = command_registry.get_group_info(group_name)
        theme_color = GROUP_THEMES.get(group_name, "white")
        icon = GROUP_ICONS.get(group_name, "🚀")
        
        # Add a header row for the group
        table.add_row(
            f"[bold {theme_color}]{icon} {group_name.upper()}[/bold {theme_color}]", 
            f"[italic]{group_info.get('description', 'No description')}[/italic]"
        )
        
        # Add each command in the group
        # Get commands directly from the Click command groups to ensure all are included
        group_obj = main.get_command(None, group_name)
        if group_obj:
            for cmd_name in sorted(group_obj.commands.keys()):
                cmd_data = command_registry.get_command_info(group_name, cmd_name)
                aliases = command_registry.get_aliases_for_command(group_name, cmd_name)
                aliases_str = ", ".join(aliases) if aliases else ""
                
                command_text = f"  {group_name} {cmd_name}"
                description = cmd_data.get('description', 'No description') if cmd_data else group_obj.commands[cmd_name].help or "No description"
                
                if aliases_str:
                    description = f"[yellow][Aliases: {aliases_str}][/yellow] {description}"
                    
                table.add_row(command_text, description)
        else:
            # Fallback to registry if Click group not found
            commands = group_info.get('commands', {})
            for cmd_name in sorted(commands.keys()):
                cmd_data = commands[cmd_name]
                aliases = command_registry.get_aliases_for_command(group_name, cmd_name)
                aliases_str = ", ".join(aliases) if aliases else ""
                
                command_text = f"  {group_name} {cmd_name}"
                description = cmd_data.get('description', 'No description')
                
                if aliases_str:
                    description = f"[yellow][Aliases: {aliases_str}][/yellow] {description}"
                    
                table.add_row(command_text, description)
    
    console.print(table)

def load_config():
    """Load configuration from YAML file."""
    config_paths = [
        Path.home() / ".starshipagentic.yaml",
        Path.home() / ".starshipagentic.yml",
        Path.home() / ".config" / "starshipagentic.yaml",
        Path.home() / ".config" / "starshipagentic.yml",
        Path("starshipagentic.yaml"),
        Path("starshipagentic.yml"),
        # Look for config in the package directory
        Path(__file__).parent / "starshipagentic.yml",
    ]
    
    for config_path in config_paths:
        if config_path.exists():
            try:
                with open(config_path, 'r') as f:
                    return yaml.safe_load(f)
            except Exception as e:
                console.print(f"[bold red]Error loading config from {config_path}: {e}[/bold red]")
                return {}
    
    return {}

def run_command_sequence(commands):
    """Run a sequence of commands from config."""
    if not commands:
        return
    
    console.print(Panel("Running Command Sequence", style="bold green"))
    
    for cmd_info in commands:
        try:
            if isinstance(cmd_info, str):
                # Simple command without args
                cmd_parts = cmd_info.split()
                console.print(f"[bold cyan]> starshipagentic {cmd_info}[/bold cyan]")
                # Execute command
                sys.argv = ["starshipagentic"] + cmd_parts
                main(standalone_mode=False)
            elif isinstance(cmd_info, dict):
                # Command with args as dict
                group_name = list(cmd_info.keys())[0]
                group_value = cmd_info[group_name]
                
                if isinstance(group_value, dict) and len(group_value) == 1:
                    # This is a nested command structure: group -> command -> options
                    cmd_name = list(group_value.keys())[0]
                    options = group_value[cmd_name]
                    
                    cmd_args = []
                    for k, v in options.items():
                        if v is True:
                            cmd_args.append(f"--{k}")
                        elif v is not None:
                            cmd_args.append(f"--{k}={v}")
                    
                    console.print(f"[bold cyan]> starshipagentic {group_name} {cmd_name} {' '.join(cmd_args)}[/bold cyan]")
                    # Execute command
                    sys.argv = ["starshipagentic", group_name, cmd_name] + cmd_args
                    main(standalone_mode=False)
                else:
                    # This is a simple command with options
                    cmd_args = []
                    for k, v in group_value.items():
                        if v is True:
                            cmd_args.append(f"--{k}")
                        elif v is not None:
                            cmd_args.append(f"--{k}={v}")
                    
                    console.print(f"[bold cyan]> starshipagentic {group_name} {' '.join(cmd_args)}[/bold cyan]")
                    # Execute command
                    sys.argv = ["starshipagentic", group_name] + cmd_args
                    main(standalone_mode=False)
        except Exception as e:
            console.print(f"[bold red]Command failed: {e}[/bold red]")
            console.print("[yellow]Continuing with next command...[/yellow]")

def interactive_mode():
    """Start interactive guided process."""
    display_welcome()
    
    # Load config
    config = load_config()
    
    # Check if we have a command sequence in config
    if config and 'commands' in config:
        run_command_sequence(config['commands'])
        return
    
    console.print(Panel("Interactive Mode", style="bold green"))
    console.print("This is your command center for AI-assisted software development.")
    
    # Show command categories first
    display_available_commands()
    
    # Option to show all commands
    console.print("\nTo see all available commands: [bold]starshipagentic --all-commands[/bold]")
    console.print("To see commands from YAML file: [bold]starshipagentic --commands-list[/bold]")
    console.print("To get started, try: [bold]starshipagentic vessel tour-ship[/bold]")

class StarshipAgenticCLI(click.Group):
    """Custom Click Group that shows commands differently."""
    
    def format_help(self, ctx, formatter):
        display_welcome()
        console.print("Type [bold]starshipagentic[/bold] to start interactive mode.\n")
        display_available_commands()
        
        # Skip the default Click help formatting
        return

def load_commands_list():
    """Load commands list from YAML file."""
    # Use the command registry to get the commands
    return command_registry._commands

@click.group(cls=StarshipAgenticCLI, invoke_without_command=True)
@click.version_option()
@click.option('--all-commands', is_flag=True, help='Show all available commands')
@click.option('--commands-list', is_flag=True, help='Show all commands from implementation')
@click.pass_context
def main(ctx, all_commands, commands_list):
    """Starship Agentic - AI-assisted software development with a Star Trek-inspired interface."""
    if commands_list:
        display_welcome()
        console.print(Panel("Complete Commands List", style="bold green"))
        
        # Get all command groups from the main CLI
        for group_name in sorted(main.commands.keys()):
            group_obj = main.commands[group_name]
            group_data = command_registry.get_group_info(group_name)
            
            theme_color = GROUP_THEMES.get(group_name, "white")
            icon = GROUP_ICONS.get(group_name, "🚀")
            console.print(f"\n[bold {theme_color}]{icon} {group_name.upper()}[/bold {theme_color}]: {group_data.get('description', '') or group_obj.help or 'No description'}")
            
            # Create a table for commands in this group
            table = Table(show_header=True, header_style=f"bold {theme_color}")
            table.add_column("Command", style=f"{theme_color}")
            table.add_column("Aliases", style="yellow")
            table.add_column("Description", style="white")
            table.add_column("Options", style="dim")
            
            # Get commands directly from the Click command group
            for cmd_name in sorted(group_obj.commands.keys()):
                cmd_obj = group_obj.commands[cmd_name]
                cmd_data = command_registry.get_command_info(group_name, cmd_name)
                
                # Get aliases from registry
                aliases = command_registry.get_aliases_for_command(group_name, cmd_name)
                aliases_str = ", ".join(aliases) if aliases else "None"
                
                # Get description from registry or Click command
                description = (cmd_data.get('description') if cmd_data else None) or cmd_obj.help or "No description"
                
                # Get options from Click command
                options = []
                for param in cmd_obj.params:
                    if isinstance(param, click.Option):
                        opt_str = f"--{param.name}"
                        if param.required:
                            opt_str += " (required)"
                        options.append(opt_str)
                
                options_str = "\n".join(options) or "None"
                
                table.add_row(
                    f"{group_name} {cmd_name}",
                    aliases_str,
                    description,
                    options_str
                )
            
            console.print(table)
        return
        
    if all_commands:
        display_welcome()
        display_all_commands()
        return
        
    if ctx.invoked_subcommand is None:
        interactive_mode()

# Enhance command groups with better help display
vessel_group = enhance_group_help(vessel.vessel_group, "vessel")
mission_group = enhance_group_help(mission.mission_group, "mission")
architecture_group = enhance_group_help(architecture.architecture_group, "architecture")
navigation_group = enhance_group_help(navigation.navigation_group, "navigation")
transmission_group = enhance_group_help(transmission.transmission_group, "transmission")
probe_group = enhance_group_help(probe.probe_group, "probe")
exploration_group = enhance_group_help(exploration.exploration_group, "exploration")
weapons_group = enhance_group_help(weapons.weapons_group, "weapons")
engineering_group = enhance_group_help(engineering.engineering_group, "engineering")
cosmic_group = enhance_group_help(cosmic.cosmic_group, "cosmic")
beam_group = enhance_group_help(beam.beam_group, "beam")
mcars_group = enhance_group_help(mcars.mcars_group, "mcars")
droid_group = enhance_group_help(droid.droid_group, "droid")

# Add command groups
main.add_command(vessel_group, "vessel")
main.add_command(mission_group, "mission")
main.add_command(architecture_group, "architecture")
main.add_command(navigation_group, "navigation")
main.add_command(transmission_group, "transmission")
main.add_command(probe_group, "probe")
main.add_command(exploration_group, "exploration")
main.add_command(weapons_group, "weapons")
main.add_command(engineering_group, "engineering")
main.add_command(cosmic_group, "cosmic")
main.add_command(beam_group, "beam")
main.add_command(mcars_group, "mcars")
main.add_command(droid_group, "droid")

if __name__ == "__main__":
    main()