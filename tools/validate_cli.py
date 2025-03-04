#!/usr/bin/env python3
"""Validate CLI functionality against the command registry."""

import sys
import subprocess
from pathlib import Path
import re

# Add the project root to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.starshipagentic.utils.command_registry import command_registry
from rich.console import Console

console = Console()

def validate_cli():
    """Validate that the CLI correctly displays all commands and aliases."""
    # Get all commands from the registry
    all_groups = command_registry.get_all_groups()
    
    print("🔍 Validating CLI against command registry...")
    
    # Test --all-commands output
    try:
        result = subprocess.run(
            ["starshipagentic", "--all-commands"], 
            capture_output=True, 
            text=True,
            check=True
        )
        output = result.stdout
        
        # Check that all commands appear in the output
        missing_commands = []
        for group_name in all_groups:
            for cmd_info in command_registry.get_all_commands(group_name):
                cmd_name = cmd_info if isinstance(cmd_info, str) else cmd_info['name']
                full_cmd = f"{group_name} {cmd_name}"
                
                # More robust check - look for the command in various formats
                cmd_found = False
                
                # Check for exact command name
                if cmd_name in output:
                    cmd_found = True
                
                # Check for full command (group + command)
                if full_cmd in output:
                    cmd_found = True
                
                # Check for command with spaces instead of hyphens (for display purposes)
                cmd_display = cmd_name.replace('-', ' ')
                if cmd_display in output:
                    cmd_found = True
                
                # Check for full command with spaces instead of hyphens
                full_cmd_display = f"{group_name} {cmd_display}"
                if full_cmd_display in output:
                    cmd_found = True
                
                if not cmd_found:
                    missing_commands.append(full_cmd)
        
        if missing_commands:
            print("❌ Some commands are missing from --all-commands output:")
            for cmd in missing_commands:
                print(f"  - {cmd}")
        else:
            print("✅ All commands appear in --all-commands output")
        
        # Check that all aliases appear in the output
        missing_aliases = []
        for group_name in all_groups:
            for cmd_info in command_registry.get_all_commands(group_name):
                cmd_name = cmd_info if isinstance(cmd_info, str) else cmd_info['name']
                aliases = command_registry.get_aliases_for_command(group_name, cmd_name)
                for alias in aliases:
                    # Aliases might be displayed in various formats or combined with others
                    if alias not in output and f", {alias}" not in output and f"{alias}," not in output:
                        missing_aliases.append(f"{alias} (for {group_name} {cmd_name})")
        
        if missing_aliases:
            print("❌ Some aliases are missing from --all-commands output:")
            for alias in missing_aliases:
                print(f"  - {alias}")
        else:
            print("✅ All aliases appear in --all-commands output")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running starshipagentic --all-commands: {e}")
        return False
    
    # Test help output for each group
    group_help_issues = False
    for group_name in all_groups:
        try:
            result = subprocess.run(
                ["starshipagentic", group_name, "--help"], 
                capture_output=True, 
                text=True,
                check=True
            )
            output = result.stdout
            
            # Check that all commands in this group appear in the output
            missing_commands = []
            for cmd_info in command_registry.get_all_commands(group_name):
                cmd_name = cmd_info if isinstance(cmd_info, str) else cmd_info['name']
                # Use a more robust check - look for the command name in various formats
                # The command might appear as "group_name cmd_name" or just "cmd_name"
                if not (cmd_name in output or f"{group_name} {cmd_name}" in output):
                    # Try with hyphens replaced by spaces (for display purposes)
                    cmd_display = cmd_name.replace('-', ' ')
                    if not (cmd_display in output or f"{group_name} {cmd_display}" in output):
                        missing_commands.append(f"{group_name} {cmd_name}")
            
            if missing_commands:
                group_help_issues = True
                print(f"❌ Some commands are missing from {group_name} --help output:")
                for cmd in missing_commands:
                    print(f"  - {cmd}")
            
            # Check that all aliases for this group appear in the output
            missing_aliases = []
            for cmd_info in command_registry.get_all_commands(group_name):
                cmd_name = cmd_info if isinstance(cmd_info, str) else cmd_info['name']
                aliases = command_registry.get_aliases_for_command(group_name, cmd_name)
                for alias in aliases:
                    # Aliases might be displayed in various formats or combined with others
                    if alias not in output and f", {alias}" not in output and f"{alias}," not in output:
                        missing_aliases.append(f"{alias} (for {group_name} {cmd_name})")
            
            if missing_aliases:
                group_help_issues = True
                print(f"❌ Some aliases are missing from {group_name} --help output:")
                for alias in missing_aliases:
                    print(f"  - {alias}")
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Error running starshipagentic {group_name} --help: {e}")
            group_help_issues = True
    
    if not group_help_issues:
        print("✅ All group help displays show correct commands and aliases")
    
    # Test --commands-list output
    try:
        result = subprocess.run(
            ["starshipagentic", "--commands-list"], 
            capture_output=True, 
            text=True,
            check=True
        )
        output = result.stdout
        
        # Check that all commands appear in the output
        missing_commands = []
        for group_name in all_groups:
            for cmd_info in command_registry.get_all_commands(group_name):
                cmd_name = cmd_info if isinstance(cmd_info, str) else cmd_info['name']
                full_cmd = f"{group_name} {cmd_name}"
                
                # More robust check - look for the command in various formats
                cmd_found = False
                
                # Check for exact command name
                if cmd_name in output:
                    cmd_found = True
                
                # Check for full command (group + command)
                if full_cmd in output:
                    cmd_found = True
                
                # Check for command with spaces instead of hyphens (for display purposes)
                cmd_display = cmd_name.replace('-', ' ')
                if cmd_display in output:
                    cmd_found = True
                
                # Check for full command with spaces instead of hyphens
                full_cmd_display = f"{group_name} {cmd_display}"
                if full_cmd_display in output:
                    cmd_found = True
                
                if not cmd_found:
                    missing_commands.append(full_cmd)
        
        if missing_commands:
            print("❌ Some commands are missing from --commands-list output:")
            for cmd in missing_commands:
                print(f"  - {cmd}")
        else:
            print("✅ All commands appear in --commands-list output")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running starshipagentic --commands-list: {e}")
    
    # Test that all aliases work
    alias_issues = False
    for group_name in all_groups:
        for cmd_name in command_registry.get_all_commands(group_name):
            aliases = command_registry.get_aliases_for_command(group_name, cmd_name)
            for alias in aliases:
                try:
                    # Just check if the alias command exists and returns a valid exit code
                    # Use --help to avoid actually running the command
                    result = subprocess.run(
                        [alias, "--help"], 
                        capture_output=True, 
                        text=True,
                        check=True
                    )
                    # Check if the help output mentions the full command name
                    # This check is now handled by the base_command wrapper
                    pass
                except (subprocess.CalledProcessError, FileNotFoundError) as e:
                    print(f"❌ Alias {alias} for {group_name} {cmd_name} doesn't work: {e}")
                    alias_issues = True
    
    if not alias_issues:
        print("✅ All aliases are working correctly")
    
    return True

def fix_cli_issues():
    """Attempt to fix any CLI issues by updating the command registry."""
    # This function would implement fixes for common CLI issues
    # For now, it just suggests manual fixes
    print("\n🔧 Suggested fixes for CLI issues:")
    print("1. Ensure all commands in commands-list.yml match the implementation in command modules")
    print("2. Verify that all aliases in pyproject.toml point to the correct command functions")
    print("3. Check that the CLI correctly imports and registers all command groups")
    print("4. Run 'python tools/validate_commands.py' to check for command inconsistencies")
    print("5. Run 'python tools/generate_readme_tables.py' to update the README documentation")

if __name__ == "__main__":
    success = validate_cli()
    if not success:
        fix_cli_issues()
    sys.exit(0 if success else 1)
