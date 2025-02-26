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

# Import command groups
from starshipagentic.commands import (
    vessel_cmds,
    mission_cmds,
    architecture_cmds,
    navigation_cmds,
    transmission_cmds,
    exploration_cmds,
    weapons_cmds,
    engineering_cmds,
    cosmic_cmds,
    git_cmds,
    mcars_cmds,
    droid_cmds,
)

console = Console()

# Command group themes/colors for consistent styling
GROUP_THEMES = {
    "vessel": "blue",
    "mission": "green",
    "architecture": "magenta",
    "navigation": "cyan",
    "transmission": "yellow",
    "exploration": "bright_blue",
    "weapons": "red",
    "engineering": "bright_green",
    "cosmic": "bright_magenta",
    "git": "bright_cyan",
    "mcars": "bright_yellow",
    "droid": "bright_white",
}

# Command group icons
GROUP_ICONS = {
    "vessel": "🚢",
    "mission": "📋",
    "architecture": "🏗️",
    "navigation": "🧭",
    "transmission": "📡",
    "exploration": "🔭",
    "weapons": "🛡️",
    "engineering": "🔧",
    "cosmic": "✨",
    "git": "📦",
    "mcars": "🔍",
    "droid": "🤖",
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
        
        # Group header with icon and styled name
        header = f"{icon} {name.upper()} COMMANDS"
        console.print(Panel(header, style=f"bold {theme_color}"))
        
        # Group description
        if group.help:
            console.print(Markdown(f"**Description:** {group.help}"))
            console.print("")
        
        # Commands table
        table = Table(show_header=True, header_style=f"bold {theme_color}")
        table.add_column("Command", style=f"{theme_color}")
        table.add_column("Description", style="white")
        table.add_column("Options", style="dim")
        
        # Add commands to table
        for cmd_name in sorted(group.commands):
            cmd = group.commands[cmd_name]
            options = []
            for param in cmd.params:
                if isinstance(param, click.Option):
                    opt_str = f"--{param.name}"
                    if param.required:
                        opt_str += " (required)"
                    options.append(opt_str)
            
            # Check for aliases
            aliases = getattr(cmd, 'aliases', [])
            command_name = f"{name} {cmd_name}"
            if aliases:
                command_name += f" (aliases: {', '.join(aliases)})"
            
            options_str = ", ".join(options) if options else "None"
            table.add_row(
                command_name,
                cmd.help or "No description",
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
    
    # Add each command group with description and example
    command_groups = [
        ("vessel", vessel_cmds.vessel_group.help, "vessel tour-ship"),
        ("mission", mission_cmds.mission_group.help, "mission define"),
        ("architecture", architecture_cmds.architecture_group.help, "architecture review-schematics"),
        ("navigation", navigation_cmds.navigation_group.help, "navigation plot-navigation"),
        ("transmission", transmission_cmds.transmission_group.help, "transmission scan-sector"),
        ("exploration", exploration_cmds.exploration_group.help, "exploration warp-speed"),
        ("weapons", weapons_cmds.weapons_group.help, "weapons shields-up"),
        ("engineering", engineering_cmds.engineering_group.help, "engineering analyze"),
        ("cosmic", cosmic_cmds.cosmic_group.help, "cosmic supernova"),
        ("git", git_cmds.git_group.help, "git teleport"),
        ("mcars", mcars_cmds.mcars_group.help, "mcars search"),
        ("droid", droid_cmds.droid_group.help, "droid droid-splain"),
    ]
    
    for group, help_text, example in command_groups:
        icon = GROUP_ICONS.get(group, "🚀")
        table.add_row(group, icon, help_text or "No description", example)
    
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
    
    # Add commands from each group
    command_groups = [
        (vessel_cmds.vessel_group, "vessel"),
        (mission_cmds.mission_group, "mission"),
        (architecture_cmds.architecture_group, "architecture"),
        (navigation_cmds.navigation_group, "navigation"),
        (transmission_cmds.transmission_group, "transmission"),
        (exploration_cmds.exploration_group, "exploration"),
        (weapons_cmds.weapons_group, "weapons"),
        (engineering_cmds.engineering_group, "engineering"),
        (cosmic_cmds.cosmic_group, "cosmic"),
        (git_cmds.git_group, "git"),
        (mcars_cmds.mcars_group, "mcars"),
        (droid_cmds.droid_group, "droid"),
    ]
    
    for group, prefix in command_groups:
        theme_color = GROUP_THEMES.get(prefix, "white")
        icon = GROUP_ICONS.get(prefix, "🚀")
        
        # Add a header row for the group
        table.add_row(f"[bold {theme_color}]{icon} {prefix.upper()}[/bold {theme_color}]", 
                     f"[italic]{group.help or 'No description'}[/italic]")
        
        # Add each command in the group
        for cmd_name in sorted(group.commands):
            cmd = group.commands[cmd_name]
            # Check for aliases
            aliases = getattr(cmd, 'aliases', [])
            command_text = f"  {prefix} {cmd_name}"
            if aliases:
                command_text += f" (aliases: {', '.join(aliases)})"
                
            table.add_row(
                command_text,
                cmd.help or "No description"
            )
    
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
        if isinstance(cmd_info, str):
            # Simple command without args
            cmd_parts = cmd_info.split()
            cmd_name = cmd_parts[0]
            cmd_args = cmd_parts[1:] if len(cmd_parts) > 1 else []
            console.print(f"[bold cyan]> starshipagentic {cmd_info}[/bold cyan]")
            # Execute command
            sys.argv = ["starshipagentic", cmd_name] + cmd_args
            main(standalone_mode=False)
        elif isinstance(cmd_info, dict):
            # Command with args as dict
            cmd_name = list(cmd_info.keys())[0]
            cmd_args = []
            for k, v in cmd_info[cmd_name].items():
                if v is True:
                    cmd_args.append(f"--{k}")
                elif v is not None:
                    cmd_args.append(f"--{k}={v}")
            
            console.print(f"[bold cyan]> starshipagentic {cmd_name} {' '.join(cmd_args)}[/bold cyan]")
            # Execute command
            sys.argv = ["starshipagentic", cmd_name] + cmd_args
            main(standalone_mode=False)

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
    commands_list_path = Path(__file__).parent / "commands-list.yml"
    if commands_list_path.exists():
        try:
            with open(commands_list_path, 'r') as f:
                return yaml.safe_load(f)
        except Exception as e:
            console.print(f"[bold red]Error loading commands list: {e}[/bold red]")
    return {}

@click.group(cls=StarshipAgenticCLI, invoke_without_command=True)
@click.version_option()
@click.option('--all-commands', is_flag=True, help='Show all available commands')
@click.option('--commands-list', is_flag=True, help='Show commands list from YAML file')
@click.pass_context
def main(ctx, all_commands, commands_list):
    """Starship Agentic - AI-assisted software development with a Star Trek-inspired interface."""
    if commands_list:
        display_welcome()
        cmd_list = load_commands_list()
        if cmd_list:
            console.print(Panel("Commands List from YAML", style="bold green"))
            for group_name, group_data in cmd_list.items():
                theme_color = GROUP_THEMES.get(group_name, "white")
                icon = GROUP_ICONS.get(group_name, "🚀")
                console.print(f"\n[bold {theme_color}]{icon} {group_name.upper()}[/bold {theme_color}]: {group_data.get('description', '')}")
                
                # Create a table for commands in this group
                table = Table(show_header=True, header_style=f"bold {theme_color}")
                table.add_column("Command", style=f"{theme_color}")
                table.add_column("Description", style="white")
                table.add_column("Options", style="dim")
                table.add_column("Aliases", style="yellow")
                
                for cmd_name, cmd_data in group_data.get('commands', {}).items():
                    options_str = "\n".join(cmd_data.get('options', [])) or "None"
                    aliases_str = ", ".join(cmd_data.get('aliases', [])) or "None"
                    table.add_row(
                        f"{group_name} {cmd_name}",
                        cmd_data.get('description', 'No description'),
                        options_str,
                        aliases_str
                    )
                
                console.print(table)
        else:
            console.print("[bold red]Commands list not found or empty.[/bold red]")
        return
        
    if all_commands:
        display_welcome()
        display_all_commands()
        return
        
    if ctx.invoked_subcommand is None:
        interactive_mode()

# Enhance command groups with better help display
vessel_group = enhance_group_help(vessel_cmds.vessel_group, "vessel")
mission_group = enhance_group_help(mission_cmds.mission_group, "mission")
architecture_group = enhance_group_help(architecture_cmds.architecture_group, "architecture")
navigation_group = enhance_group_help(navigation_cmds.navigation_group, "navigation")
transmission_group = enhance_group_help(transmission_cmds.transmission_group, "transmission")
exploration_group = enhance_group_help(exploration_cmds.exploration_group, "exploration")
weapons_group = enhance_group_help(weapons_cmds.weapons_group, "weapons")
engineering_group = enhance_group_help(engineering_cmds.engineering_group, "engineering")
cosmic_group = enhance_group_help(cosmic_cmds.cosmic_group, "cosmic")
git_group = enhance_group_help(git_cmds.git_group, "git")
mcars_group = enhance_group_help(mcars_cmds.mcars_group, "mcars")
droid_group = enhance_group_help(droid_cmds.droid_group, "droid")

# Add command groups
main.add_command(vessel_group, "vessel")
main.add_command(mission_group, "mission")
main.add_command(architecture_group, "architecture")
main.add_command(navigation_group, "navigation")
main.add_command(transmission_group, "transmission")
main.add_command(exploration_group, "exploration")
main.add_command(weapons_group, "weapons")
main.add_command(engineering_group, "engineering")
main.add_command(cosmic_group, "cosmic")
main.add_command(git_group, "git")
main.add_command(mcars_group, "mcars")
main.add_command(droid_group, "droid")

if __name__ == "__main__":
    main()
