# [AUTO-GENERATED GROUP HELP REGISTER START]
import importlib
GROUP_NAMES = ['fleet_commander', 'number_two', 'engineering_officer', 'navigation_officer', 'communications_officer', 'insterstellar_officer', 'captains_orders', 'tactical_officer', 'maintenance_officer', 'red_buttons', 'gitmaster', 'mcars', 'droids']
for group in GROUP_NAMES:
    mod = importlib.import_module(f'starshipagentic.commands.{group}')
    group_obj = getattr(mod, f'{group}_group', None)
    if group_obj is None:
        continue
    enhanced = enhance_group_help(group_obj, group)
    main.add_command(enhanced, group)
# [AUTO-GENERATED GROUP HELP REGISTER END]
# [AUTO-GENERATED GROUP THEMES AND ICONS START]
GROUP_THEMES = {
    "fleet_commander": "white",
    "number_two": "white",
    "engineering_officer": "white",
    "navigation_officer": "white",
    "communications_officer": "white",
    "insterstellar_officer": "white",
    "captains_orders": "white",
    "tactical_officer": "white",
    "maintenance_officer": "white",
    "red_buttons": "white",
    "gitmaster": "white",
    "mcars": "white",
    "droids": "white",
}

GROUP_ICONS = {
    "fleet_commander": "⚙️",
    "number_two": "⚙️",
    "engineering_officer": "⚙️",
    "navigation_officer": "⚙️",
    "communications_officer": "⚙️",
    "insterstellar_officer": "⚙️",
    "captains_orders": "⚙️",
    "tactical_officer": "⚙️",
    "maintenance_officer": "⚙️",
    "red_buttons": "⚙️",
    "gitmaster": "⚙️",
    "mcars": "⚙️",
    "droids": "⚙️",
}

# [AUTO-GENERATED GROUP THEMES AND ICONS END]
# [AUTO-GENERATED COMMAND IMPORTS START]
from starshipagentic.commands.fleet_commander import run_group as fleet_commander
from starshipagentic.commands.number_two import run_group as number_two
from starshipagentic.commands.engineering_officer import run_group as engineering_officer
from starshipagentic.commands.navigation_officer import run_group as navigation_officer
from starshipagentic.commands.communications_officer import run_group as communications_officer
from starshipagentic.commands.insterstellar_officer import run_group as insterstellar_officer
from starshipagentic.commands.captains_orders import run_group as captains_orders
from starshipagentic.commands.tactical_officer import run_group as tactical_officer
from starshipagentic.commands.maintenance_officer import run_group as maintenance_officer
from starshipagentic.commands.red_buttons import run_group as red_buttons
from starshipagentic.commands.gitmaster import run_group as gitmaster
from starshipagentic.commands.mcars import run_group as mcars
from starshipagentic.commands.droids import run_group as droids
from starshipagentic.commands.fleet_commander.tour_ship.cli import tour_ship_command as tour_ship
from starshipagentic.commands.fleet_commander.tour_ship.cli import tour_ship_command as tour
from starshipagentic.commands.fleet_commander.commission_ship.cli import commission_ship_command as commission_ship
from starshipagentic.commands.fleet_commander.commission_ship.cli import commission_ship_command as commission
from starshipagentic.commands.fleet_commander.visualize_ship.cli import visualize_ship_command as visualize_ship
from starshipagentic.commands.number_two.mission_brief.cli import mission_brief_command as mission_brief
from starshipagentic.commands.number_two.mission_brief.cli import mission_brief_command as mission
from starshipagentic.commands.number_two.expand_mission.cli import expand_mission_command as expand_mission
from starshipagentic.commands.number_two.expand_mission.cli import expand_mission_command as expand
from starshipagentic.commands.engineering_officer.review_schematics.cli import review_schematics_command as review_schematics
from starshipagentic.commands.engineering_officer.review_schematics.cli import review_schematics_command as schematics
from starshipagentic.commands.engineering_officer.calibrate_technology.cli import calibrate_technology_command as calibrate_technology
from starshipagentic.commands.engineering_officer.calibrate_technology.cli import calibrate_technology_command as calibrate
from starshipagentic.commands.navigation_officer.plot_navigation.cli import plot_navigation_command as plot_navigation
from starshipagentic.commands.navigation_officer.plot_navigation.cli import plot_navigation_command as navigation
from starshipagentic.commands.navigation_officer.set_waypoints.cli import set_waypoints_command as set_waypoints
from starshipagentic.commands.navigation_officer.set_waypoints.cli import set_waypoints_command as waypoints
from starshipagentic.commands.communications_officer.authorize_codes.cli import authorize_codes_command as authorize_codes
from starshipagentic.commands.communications_officer.authorize_codes.cli import authorize_codes_command as authorize
from starshipagentic.commands.communications_officer.scan_sector.cli import scan_sector_command as scan_sector
from starshipagentic.commands.communications_officer.scan_sector.cli import scan_sector_command as scan
from starshipagentic.commands.communications_officer.receive_transmission.cli import receive_transmission_command as receive_transmission
from starshipagentic.commands.communications_officer.receive_transmission.cli import receive_transmission_command as transmission
from starshipagentic.commands.insterstellar_officer.map_planet.cli import map_planet_command as map_planet
from starshipagentic.commands.insterstellar_officer.map_planet.cli import map_planet_command as map
from starshipagentic.commands.insterstellar_officer.build_landing_zone.cli import build_landing_zone_command as build_landing_zone
from starshipagentic.commands.insterstellar_officer.build_landing_zone.cli import build_landing_zone_command as buildlz
from starshipagentic.commands.insterstellar_officer.fabricate_infrastructure.cli import fabricate_infrastructure_command as fabricate_infrastructure
from starshipagentic.commands.insterstellar_officer.fabricate_infrastructure.cli import fabricate_infrastructure_command as fabricate
from starshipagentic.commands.captains_orders.warp_speed.cli import warp_speed_command as warp_speed
from starshipagentic.commands.captains_orders.warp_speed.cli import warp_speed_command as warp
from starshipagentic.commands.captains_orders.trycoder.cli import trycoder_command as trycoder
from starshipagentic.commands.captains_orders.engage.cli import engage_command as engage
from starshipagentic.commands.tactical_officer.fire_photons.cli import fire_photons_command as fire_photons
from starshipagentic.commands.tactical_officer.fire_photons.cli import fire_photons_command as photons
from starshipagentic.commands.tactical_officer.aim_lasers.cli import aim_lasers_command as aim_lasers
from starshipagentic.commands.tactical_officer.aim_lasers.cli import aim_lasers_command as lasers
from starshipagentic.commands.tactical_officer.shields_up.cli import shields_up_command as shields_up
from starshipagentic.commands.tactical_officer.shields_up.cli import shields_up_command as shields
from starshipagentic.commands.maintenance_officer.create_checkpoint.cli import create_checkpoint_command as create_checkpoint
from starshipagentic.commands.maintenance_officer.create_checkpoint.cli import create_checkpoint_command as checkpoint
from starshipagentic.commands.maintenance_officer.restore_checkpoint.cli import restore_checkpoint_command as restore_checkpoint
from starshipagentic.commands.maintenance_officer.restore_checkpoint.cli import restore_checkpoint_command as restore
from starshipagentic.commands.maintenance_officer.inspect_vessel.cli import inspect_vessel_command as inspect_vessel
from starshipagentic.commands.maintenance_officer.inspect_vessel.cli import inspect_vessel_command as inspect
from starshipagentic.commands.maintenance_officer.complexity_report.cli import complexity_report_command as complexity_report
from starshipagentic.commands.maintenance_officer.complexity_report.cli import complexity_report_command as complexity
from starshipagentic.commands.red_buttons.supernova.cli import supernova_command as supernova
from starshipagentic.commands.gitmaster.teleport.cli import teleport_command as teleport
from starshipagentic.commands.mcars.search.cli import search_command as search
from starshipagentic.commands.mcars.transport.cli import transport_command as transport
from starshipagentic.commands.droids.droid_splain.cli import droid_splain_command as droid_splain
from starshipagentic.commands.droids.droid_splain.cli import droid_splain_command as droid
from starshipagentic.commands.droids.man_splain.cli import man_splain_command as man_splain
from starshipagentic.commands.droids.man_splain.cli import man_splain_command as splain
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

console = Console()

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

if __name__ == "__main__":
    main()