#!/usr/bin/env python3
"""
Starship Agentic CLI - Static Content
This file contains the static parts of the CLI that don't change during generation.
"""

import click
from rich.console import Console
from rich.panel import Panel

console = Console()

def enhance_group_help(group, name):
    """Enhance a command group with better help text and rich formatting."""
    from rich.table import Table
    from rich.console import Console
    from rich.text import Text
    from starshipagentic.utils.command_registry import CommandRegistry
    
    # Create a custom callback for the help option
    def custom_help_callback(ctx, param, value):
        if not value or ctx.resilient_parsing:
            return
        
        console = Console()
        
        # Get group info from registry
        registry = CommandRegistry()
        group_info = registry.get_group_info(name)
        
        # Create a title panel
        title = f"[bold cyan]{name.upper()}[/bold cyan]: {group_info.get('description', f'Commands for {name.replace('_', ' ')}')}"
        console.print(f"\n{title}\n")
        
        # Create a table for commands
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Command", style="green")
        table.add_column("Aliases", style="yellow")
        table.add_column("Description", style="cyan")
        
        # Add rows for each command
        commands = registry.get_all_commands(name)
        for cmd_name, cmd_info in commands.items():
            aliases = registry.get_aliases_for_command(name, cmd_name)
            alias_str = ", ".join(aliases) if aliases else ""
            description = cmd_info.get("description", "")
            table.add_row(cmd_name, alias_str, description)
        
        console.print(table)
        console.print("\nUse [bold]<command> --help[/bold] for detailed information about a specific command.\n")
        ctx.exit()
    
    # Override the help option to use our custom callback
    for param in group.params:
        if param.name == 'help':
            param.callback = custom_help_callback
            break
    
    # Set a basic help text for when --help isn't used
    group.help = f"[{name.upper()}] Commands for {name.replace('_', ' ')}"
    
    return group

@click.group(invoke_without_command=True)
@click.option("--all-commands", is_flag=True, help="Display all available commands")
@click.option("--commands-list", is_flag=True, help="Display commands from commands-list.yml")
@click.pass_context
def main(ctx, all_commands, commands_list):
    """Starship Agentic CLI - Your AI-powered command center."""
    if ctx.invoked_subcommand is None:
        console.print(Panel("Welcome to Starship Agentic", title="🚀"))
        if all_commands:
            console.print("All commands would be displayed here")
        elif commands_list:
            console.print("Commands from commands-list.yml would be displayed here")
        else:
            console.print("Use --help for more information")

# Import and register dynamic groups immediately when this module is imported
from starshipagentic.cli_generated import register_dynamic_groups
register_dynamic_groups()

if __name__ == "__main__":
    main()
