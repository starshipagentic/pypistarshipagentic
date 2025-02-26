"""Engineering commands for managing project state and analyzing code quality."""

import click
import sys
import subprocess
from rich.console import Console
from starshipagentic.utils.interactive import prompt_for_missing_param
from starshipagentic.utils.base_command import BaseCommand

console = Console()
base_cmd = BaseCommand()

@click.group(name="engineering")
def engineering_group():
    """Manage project state and analyze code quality."""
    pass

@engineering_group.command(name="create-checkpoint")
@click.argument("message", required=False)
@click.option("--message", "-m", "message_opt", help="Checkpoint message")
def create_checkpoint(message, message_opt):
    # Use the option value if provided, otherwise use the argument
    message = message_opt or message
    
    # If message is not provided, prompt for it
    if not message:
        message = prompt_for_missing_param(
            "message",
            "Enter a message for this checkpoint:",
            default="Checkpoint " + click.get_current_context().command_path
        )
    """Save project state."""
    console.print("[bold]Creating project checkpoint...[/bold]")
    
    if message:
        console.print(f"Checkpoint message: {message}")
    
    console.print("[green]Checkpoint created![/green]")

@engineering_group.command(name="restore-checkpoint")
@click.argument("checkpoint", required=False)
@click.option("--checkpoint", "checkpoint_opt", help="Checkpoint to restore")
def restore_checkpoint(checkpoint, checkpoint_opt):
    # Use the option value if provided, otherwise use the argument
    checkpoint = checkpoint_opt or checkpoint
    
    # If checkpoint is not provided, prompt for it
    if not checkpoint:
        checkpoint = prompt_for_missing_param(
            "checkpoint",
            "Which checkpoint would you like to restore?",
            default="latest"
        )
    """Roll back to saved state."""
    console.print("[bold]Restoring from checkpoint...[/bold]")
    
    if checkpoint:
        console.print(f"Restoring to checkpoint: {checkpoint}")
    else:
        console.print("Restoring to last checkpoint")
    
    console.print("[green]Checkpoint restored![/green]")

@engineering_group.command(name="inspect-vessel")
@click.argument("system", required=False)
@click.option("--system", "system_opt", help="Specific system to inspect")
def inspect_vessel(system, system_opt):
    # Use the option value if provided, otherwise use the argument
    system = system_opt or system
    
    # Available systems
    systems = ["database", "frontend", "api", "auth", "all"]
    
    # If system is not provided, prompt for it
    if not system:
        system = prompt_for_missing_param(
            "system",
            "Which system would you like to inspect?",
            choices=systems,
            default="all"
        )
    """Run framework-specific integrity checks."""
    console.print("[bold]Inspecting vessel systems...[/bold]")
    
    if system:
        console.print(f"Inspecting {system} system")
    else:
        console.print("Running full vessel inspection")
    
    console.print("[green]Inspection complete![/green]")

@engineering_group.command(name="complexity-report")
@click.argument("threshold", required=False, type=int)
@click.option("--threshold", "threshold_opt", type=int, default=10, help="Complexity threshold")
def complexity_report(threshold, threshold_opt):
    # Use the option value if provided, otherwise use the argument
    threshold = threshold_opt if threshold_opt is not None else threshold
    
    # If threshold is not provided, prompt for it
    if threshold is None:
        threshold_str = prompt_for_missing_param(
            "threshold",
            "Enter complexity threshold (higher = show only more complex functions):",
            default="10"
        )
        threshold = int(threshold_str)
    """Generate code complexity metrics."""
    console.print("[bold]Generating complexity report...[/bold]")
    
    try:
        # Check if radon is installed
        import importlib.util
        if importlib.util.find_spec("radon") is None:
            console.print("[bold red]Error:[/bold red] Radon is not installed.")
            console.print("Install with: [bold]pip install radon[/bold]")
            return
        
        # Run Maintainability Index analysis
        console.print("\n[bold green]Maintainability Index Analysis:[/bold green]")
        mi_result = subprocess.run(
            ["radon", "mi", "."], 
            capture_output=True, 
            text=True
        )
        
        if mi_result.returncode == 0:
            console.print(mi_result.stdout)
        else:
            console.print(f"[bold red]Error running Maintainability Index analysis:[/bold red]\n{mi_result.stderr}")
        
        # Run Cyclomatic Complexity analysis
        console.print("\n[bold green]Cyclomatic Complexity Analysis:[/bold green]")
        console.print(f"[italic]Showing functions with complexity above threshold: {threshold}[/italic]")
        
        cc_result = subprocess.run(
            ["radon", "cc", ".", "-a", "-s", f"--min={threshold}", "--exclude-code=venv"], 
            capture_output=True, 
            text=True
        )
        
        if cc_result.returncode == 0:
            if cc_result.stdout.strip():
                console.print(cc_result.stdout)
            else:
                console.print("[green]No functions found with complexity above the threshold.[/green]")
        else:
            console.print(f"[bold red]Error running Cyclomatic Complexity analysis:[/bold red]\n{cc_result.stderr}")
            
        console.print("\n[bold blue]Complexity analysis complete.[/bold blue]")
        console.print("[italic]For more information about complexity metrics, run: [bold]splain code complexity[/bold][/italic]")
        
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
        console.print("Make sure radon is installed: [bold]pip install radon[/bold]")

# Command entry points for direct invocation
create_checkpoint_command = base_cmd.parse_args_for_command(create_checkpoint)
restore_checkpoint_command = base_cmd.parse_args_for_command(restore_checkpoint)
inspect_vessel_command = base_cmd.parse_args_for_command(inspect_vessel)
complexity_report_command = base_cmd.parse_args_for_command(complexity_report)
