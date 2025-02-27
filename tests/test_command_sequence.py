"""Test script to verify command sequence execution."""

import sys
import os
import tempfile
import yaml
from rich.console import Console
from rich.panel import Panel
import click

# Import the run_command_sequence function
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from starshipagentic.cli import run_command_sequence

console = Console()

def create_test_config(config_data):
    """Create a temporary config file with the given data."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as temp:
        yaml.dump(config_data, temp)
        return temp.name

def test_string_commands():
    """Test command sequences with string commands."""
    console.print(Panel("Testing String Commands", style="bold green"))
    
    config = {
        'commands': [
            "vessel tour-ship",
            "vessel visualize-ship --ship=enterprise"
        ]
    }
    
    config_path = create_test_config(config)
    console.print(f"Created test config at: {config_path}")
    
    try:
        with open(config_path, 'r') as f:
            data = yaml.safe_load(f)
        
        run_command_sequence(data['commands'])
        return True
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        return False
    finally:
        os.unlink(config_path)

def test_dict_commands():
    """Test command sequences with dictionary commands."""
    console.print(Panel("Testing Dictionary Commands", style="bold yellow"))
    
    config = {
        'commands': [
            {"vessel": {
                "commission-ship": {
                    "template": "django-galaxy",
                    "name": "test-project"
                }
            }}
        ]
    }
    
    config_path = create_test_config(config)
    console.print(f"Created test config at: {config_path}")
    
    try:
        with open(config_path, 'r') as f:
            data = yaml.safe_load(f)
        
        run_command_sequence(data['commands'])
        return True
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        return False
    finally:
        os.unlink(config_path)

def test_mixed_commands():
    """Test command sequences with mixed string and dictionary commands."""
    console.print(Panel("Testing Mixed Commands", style="bold blue"))
    
    config = {
        'commands': [
            "vessel tour-ship",
            {"vessel": {
                "commission-ship": {
                    "template": "django-galaxy",
                    "name": "test-project"
                }
            }},
            "mission mission-brief"
        ]
    }
    
    config_path = create_test_config(config)
    console.print(f"Created test config at: {config_path}")
    
    try:
        with open(config_path, 'r') as f:
            data = yaml.safe_load(f)
        
        run_command_sequence(data['commands'])
        return True
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        return False
    finally:
        os.unlink(config_path)

@click.command()
@click.option("--section", help="Test section to run (string, dict, mixed, all)")
def main(section):
    """Run command sequence tests."""
    results = []
    
    if section in (None, "all", "string"):
        console.print("[bold]Testing string commands...[/bold]")
        success = test_string_commands()
        results.append(("String commands", success))
    
    if section in (None, "all", "dict"):
        console.print("[bold]Testing dictionary commands...[/bold]")
        success = test_dict_commands()
        results.append(("Dictionary commands", success))
    
    if section in (None, "all", "mixed"):
        console.print("[bold]Testing mixed commands...[/bold]")
        success = test_mixed_commands()
        results.append(("Mixed commands", success))
    
    # Display results
    console.print("\n[bold]Test Results:[/bold]")
    for test, success in results:
        result = "[green]✓ Passed[/green]" if success else "[red]✗ Failed[/red]"
        console.print(f"{test}: {result}")
    
    # Check if any tests failed
    if any(not success for _, success in results):
        console.print("[bold red]Some tests failed![/bold red]")
        sys.exit(1)
    else:
        console.print("[bold green]All tests passed![/bold green]")

if __name__ == "__main__":
    main()
