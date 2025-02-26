"""Main CLI entry point for Starship Agentic."""

import click
import sys
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

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
    console.print("Type [bold]starshipagentic --help[/bold] to see available commands.\n")

def interactive_mode():
    """Start interactive guided process."""
    display_welcome()
    
    console.print("[bold]Starting interactive mode...[/bold]")
    console.print("This feature will guide you through the development process step by step.")
    console.print("(Interactive mode implementation coming soon)")
    
    # TODO: Implement interactive mode with step-by-step guidance
    # For now, just display available command groups
    
    console.print("\n[bold]Available command groups:[/bold]")
    console.print("  vessel       - Initialize and select project templates")
    console.print("  mission      - Define and expand project requirements")
    console.print("  architecture - Review and configure system architecture")
    console.print("  navigation   - Plan feature implementation")
    console.print("  transmission - Manage external data and API connections")
    console.print("  exploration  - Execute and test your implementation")
    console.print("  weapons      - Remove problematic code and tests")
    console.print("  engineering  - Manage project state and analyze code quality")
    console.print("  cosmic       - Special operations")
    console.print("  git          - Git-related operations")
    console.print("  mcars        - Code repository and search system")
    console.print("  droid        - Explanation and assistance commands")
    
    console.print("\nTo get started, try: [bold]starshipagentic vessel tour-ship[/bold]")

@click.group(invoke_without_command=True)
@click.version_option()
@click.pass_context
def main(ctx):
    """Starship Agentic - AI-assisted software development with a Star Trek-inspired interface."""
    if ctx.invoked_subcommand is None:
        interactive_mode()

# Add command groups
main.add_command(vessel_cmds.vessel_group, "vessel")
main.add_command(mission_cmds.mission_group, "mission")
main.add_command(architecture_cmds.architecture_group, "architecture")
main.add_command(navigation_cmds.navigation_group, "navigation")
main.add_command(transmission_cmds.transmission_group, "transmission")
main.add_command(exploration_cmds.exploration_group, "exploration")
main.add_command(weapons_cmds.weapons_group, "weapons")
main.add_command(engineering_cmds.engineering_group, "engineering")
main.add_command(cosmic_cmds.cosmic_group, "cosmic")
main.add_command(git_cmds.git_group, "git")
main.add_command(mcars_cmds.mcars_group, "mcars")
main.add_command(droid_cmds.droid_group, "droid")

if __name__ == "__main__":
    main()
