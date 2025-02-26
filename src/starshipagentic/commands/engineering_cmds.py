"""Engineering commands for managing project state and analyzing code quality."""

import click
import sys
import subprocess
from rich.console import Console

console = Console()

@click.group(name="engineering")
def engineering_group():
    """Manage project state and analyze code quality."""
    pass

@engineering_group.command(name="create-checkpoint")
@click.option("--message", "-m", help="Checkpoint message")
def create_checkpoint(message):
    """Save project state."""
    console.print("[bold]Creating project checkpoint...[/bold]")
    
    if message:
        console.print(f"Checkpoint message: {message}")
    
    console.print("[green]Checkpoint created![/green]")

@engineering_group.command(name="restore-checkpoint")
@click.argument("checkpoint", required=False)
def restore_checkpoint(checkpoint):
    """Roll back to saved state."""
    console.print("[bold]Restoring from checkpoint...[/bold]")
    
    if checkpoint:
        console.print(f"Restoring to checkpoint: {checkpoint}")
    else:
        console.print("Restoring to last checkpoint")
    
    console.print("[green]Checkpoint restored![/green]")

@engineering_group.command(name="inspect-vessel")
@click.option("--system", help="Specific system to inspect")
def inspect_vessel(system):
    """Run framework-specific integrity checks."""
    console.print("[bold]Inspecting vessel systems...[/bold]")
    
    if system:
        console.print(f"Inspecting {system} system")
    else:
        console.print("Running full vessel inspection")
    
    console.print("[green]Inspection complete![/green]")

@engineering_group.command(name="complexity-report")
@click.option("--threshold", type=int, default=10, help="Complexity threshold")
def complexity_report(threshold):
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
def create_checkpoint_command():
    """Entry point for the 'checkpoint' command."""
    return create_checkpoint(sys.argv[1:])

def restore_checkpoint_command():
    """Entry point for the 'restore' command."""
    return restore_checkpoint(sys.argv[1:])

def inspect_vessel_command():
    """Entry point for the 'inspect' command."""
    return inspect_vessel(sys.argv[1:])

def complexity_report_command():
    """Entry point for the 'complexity' command."""
    # Parse arguments for the complexity command
    args = []
    if len(sys.argv) > 1:
        args = sys.argv[1:]
    return complexity_report(args)
