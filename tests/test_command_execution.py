"""Test script to verify command execution and error handling."""

import sys
import subprocess
import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def run_command(command):
    """Run a command and return the result."""
    console.print(f"[bold cyan]Testing: starshipagentic {command}[/bold cyan]")
    
    try:
        result = subprocess.run(
            f"starshipagentic {command}",
            shell=True,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            console.print("[green]✓ Command succeeded[/green]")
            return True, result.stdout
        else:
            console.print(f"[red]✗ Command failed with code {result.returncode}[/red]")
            console.print(f"Error: {result.stderr}")
            return False, result.stderr
    except Exception as e:
        console.print(f"[red]✗ Exception: {str(e)}[/red]")
        return False, str(e)

def test_basic_commands():
    """Test basic command functionality."""
    console.print(Panel("Testing Basic Commands", style="bold green"))
    
    commands = [
        "vessel tour-ship",
        "vessel commission-ship --template=django-galaxy --name=test-project",
        "vessel visualize-ship --ship=enterprise",
        "mission define",
        "architecture review-schematics --type=system"
    ]
    
    results = []
    for cmd in commands:
        success, output = run_command(cmd)
        results.append((cmd, success))
    
    return results

def test_aliases():
    """Test command aliases."""
    console.print(Panel("Testing Command Aliases", style="bold yellow"))
    
    aliases = [
        "tour",  # Alias for vessel tour-ship
        "commission --template=django-galaxy --name=test-project",  # Alias for vessel commission-ship
        "schematics --type=system"  # Alias for architecture review-schematics
    ]
    
    results = []
    for cmd in aliases:
        success, output = run_command(cmd)
        results.append((cmd, success))
    
    return results

def test_error_handling():
    """Test error handling for invalid commands."""
    console.print(Panel("Testing Error Handling", style="bold red"))
    
    invalid_commands = [
        "vessel --commission-ship",  # Option instead of command
        "vesssel tour-ship",  # Typo in command group
        "vessel tour-ships",  # Typo in command name
        "vessel commission-ship --templat=django-galaxy"  # Typo in option name
    ]
    
    results = []
    for cmd in invalid_commands:
        success, output = run_command(cmd)
        # For error tests, we expect failure
        results.append((cmd, not success))
    
    return results

def test_config_commands():
    """Test commands from configuration files."""
    console.print(Panel("Testing Configuration Commands", style="bold blue"))
    
    # Test the interactive mode which should load from config
    success, output = run_command("")
    
    return [("interactive mode", success)]

def display_results(all_results):
    """Display test results in a table."""
    table = Table(title="Command Test Results")
    table.add_column("Command", style="cyan")
    table.add_column("Result", style="green")
    
    for cmd, success in all_results:
        result = "[green]✓ Passed[/green]" if success else "[red]✗ Failed[/red]"
        table.add_row(cmd, result)
    
    console.print(table)

@click.command()
@click.option("--section", help="Test section to run (basic, aliases, errors, config, all)")
def main(section):
    """Run command execution tests."""
    all_results = []
    
    if section in (None, "all", "basic"):
        all_results.extend(test_basic_commands())
    
    if section in (None, "all", "aliases"):
        all_results.extend(test_aliases())
    
    if section in (None, "all", "errors"):
        all_results.extend(test_error_handling())
    
    if section in (None, "all", "config"):
        all_results.extend(test_config_commands())
    
    display_results(all_results)
    
    # Count failures
    failures = sum(1 for _, success in all_results if not success)
    if failures > 0:
        console.print(f"[bold red]{failures} tests failed[/bold red]")
        sys.exit(1)
    else:
        console.print("[bold green]All tests passed![/bold green]")

if __name__ == "__main__":
    main()
