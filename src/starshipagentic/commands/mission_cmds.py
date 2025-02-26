"""Mission commands for defining and expanding project requirements."""

import click
import sys
from rich.console import Console
from starshipagentic.utils.interactive import prompt_for_missing_param
from starshipagentic.utils.base_command import BaseCommand

console = Console()
base_cmd = BaseCommand()

@click.group(name="mission")
def mission_group():
    """Define and expand project requirements."""
    pass

@mission_group.command(name="mission-brief")
@click.argument("idea", required=False)
@click.option("--idea", "idea_opt", help="Project idea description")
@click.option("--detailed", is_flag=True, help="Generate detailed documentation")
def mission_brief(idea, idea_opt, detailed):
    """Generate initial project documentation."""
    # Use the option value if provided, otherwise use the argument
    idea = idea_opt or idea
    
    # If idea is not provided, prompt for it
    if not idea:
        idea = prompt_for_missing_param(
            "idea",
            "What is your mission (project idea)?",
            default="A web application for task management"
        )
    
    console.print(f"[bold]Generating mission brief for: {idea}[/bold]")
    
    if detailed:
        console.print("Creating detailed documentation...")
    else:
        console.print("Creating standard documentation...")
    
    console.print("[green]Mission brief generated![/green]")

@mission_group.command(name="expand-mission")
@click.argument("focus", required=False)
@click.option("--focus", "focus_opt", help="Area to expand upon")
def expand_mission(focus, focus_opt):
    """Elaborate on project requirements."""
    # Use the option value if provided, otherwise use the argument
    focus = focus_opt or focus
    
    # Available focus areas
    focus_areas = [
        "user-stories", "technical-requirements", "api-endpoints", 
        "database-schema", "security", "deployment"
    ]
    
    # If focus is not provided, prompt for it
    if not focus:
        focus = prompt_for_missing_param(
            "focus",
            "Which aspect of the mission would you like to expand?",
            choices=focus_areas,
            default="user-stories"
        )
    
    console.print(f"[bold]Expanding mission details for: {focus}[/bold]")
    console.print("[green]Mission expanded successfully![/green]")

# Command entry points for direct invocation
mission_brief_command = base_cmd.parse_args_for_command(mission_brief)
expand_mission_command = base_cmd.parse_args_for_command(expand_mission)
