#!/usr/bin/env python3
"""Validate command implementations against commands-list.yml."""

import sys
import os
import inspect
from pathlib import Path
import importlib
import click

# Add the project root to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.starshipagentic.utils.command_registry import command_registry

def get_implemented_commands():
    """Get all implemented commands from the codebase."""
    implemented_commands = {}
    
    # Import all command modules
    from src.starshipagentic.commands import (
        vessel_cmds,
        mission_cmds,
        architecture_cmds,
        navigation_cmds,
        transmission_cmds,
        send_probe_cmds,
        exploration_cmds,
        weapons_cmds,
        engineering_cmds,
        cosmic_cmds,
        git_cmds,
        mcars_cmds,
        droid_cmds,
    )
    
    # List of all command modules
    command_modules = [
        ("vessel", vessel_cmds),
        ("mission", mission_cmds),
        ("architecture", architecture_cmds),
        ("navigation", navigation_cmds),
        ("transmission", transmission_cmds),
        ("send_probe", send_probe_cmds),
        ("exploration", exploration_cmds),
        ("weapons", weapons_cmds),
        ("engineering", engineering_cmds),
        ("cosmic", cosmic_cmds),
        ("git", git_cmds),
        ("mcars", mcars_cmds),
        ("droid", droid_cmds),
    ]
    
    # Extract commands from each module
    for group_name, module in command_modules:
        group_obj = getattr(module, f"{group_name}_group", None)
        if not group_obj:
            continue
            
        implemented_commands[group_name] = {
            "description": group_obj.help,
            "commands": {}
        }
        
        # Get commands from the group
        for cmd_name, cmd_obj in group_obj.commands.items():
            implemented_commands[group_name]["commands"][cmd_name] = {
                "description": cmd_obj.help,
                "aliases": [],  # Will be populated from pyproject.toml
                "options": [
                    f"--{param.name}" for param in cmd_obj.params 
                    if isinstance(param, click.Option)
                ]
            }
    
    # Add aliases from pyproject.toml
    try:
        import tomli
    except ImportError:
        import tomllib as tomli
        
    pyproject_path = Path(__file__).parent.parent / "pyproject.toml"
    if pyproject_path.exists():
        with open(pyproject_path, "rb") as f:
            pyproject = tomli.load(f)
        
        # Extract aliases from project.scripts
        scripts = pyproject.get("project", {}).get("scripts", {})
        for alias, target in scripts.items():
            # Skip the main command
            if alias == "starshipagentic":
                continue
                
            # Parse the target to get the group and command
            # Format is typically: "starshipagentic.commands.group_cmds:command_name_command"
            try:
                module_path, func_name = target.split(":")
                group_name = module_path.split(".")[-1].replace("_cmds", "")
                
                # The command function name typically ends with "_command"
                # and is derived from the actual command name
                cmd_func_name = func_name.replace("_command", "")
                
                # Convert function name to command name (replace underscores with hyphens)
                cmd_name = cmd_func_name.replace("_", "-")
                
                # Add the alias to the appropriate command
                if group_name in implemented_commands:
                    for command_name, command_data in implemented_commands[group_name]["commands"].items():
                        # Check if this is the right command by comparing hyphenated names
                        if command_name.replace("-", "_") == cmd_func_name:
                            implemented_commands[group_name]["commands"][command_name]["aliases"].append(alias)
                            break
            except (ValueError, KeyError, IndexError):
                # Skip entries that don't match the expected format
                continue
    
    return implemented_commands

def validate_commands():
    """Validate that all commands in YAML have implementations and vice versa."""
    # Get documented commands from registry
    documented_commands = command_registry._commands
    
    # Get implemented commands from codebase
    implemented_commands = get_implemented_commands()
    
    # Check for documented but not implemented
    missing_implementations = []
    for group_name, group_data in documented_commands.items():
        if group_name not in implemented_commands:
            missing_implementations.append(f"Group '{group_name}' is documented but not implemented")
            continue
            
        for cmd_name in group_data.get("commands", {}):
            if cmd_name not in implemented_commands[group_name]["commands"]:
                missing_implementations.append(f"Command '{group_name} {cmd_name}' is documented but not implemented")
    
    # Check for implemented but not documented
    missing_documentation = []
    for group_name, group_data in implemented_commands.items():
        if group_name not in documented_commands:
            missing_documentation.append(f"Group '{group_name}' is implemented but not documented")
            continue
            
        for cmd_name in group_data["commands"]:
            if cmd_name not in documented_commands[group_name].get("commands", {}):
                missing_documentation.append(f"Command '{group_name} {cmd_name}' is implemented but not documented")
    
    # Check for alias consistency
    alias_inconsistencies = []
    for group_name, group_data in documented_commands.items():
        if group_name not in implemented_commands:
            continue
            
        for cmd_name, cmd_data in group_data.get("commands", {}).items():
            if cmd_name not in implemented_commands[group_name]["commands"]:
                continue
                
            doc_aliases = set(cmd_data.get("aliases", []))
            impl_aliases = set(implemented_commands[group_name]["commands"][cmd_name].get("aliases", []))
            
            if doc_aliases != impl_aliases:
                alias_inconsistencies.append(
                    f"Command '{group_name} {cmd_name}' has inconsistent aliases: "
                    f"Documented: {doc_aliases}, Implemented: {impl_aliases}"
                )
    
    # Print results
    if not missing_implementations and not missing_documentation and not alias_inconsistencies:
        print("✅ All commands are properly documented and implemented!")
        return True
    
    if missing_implementations:
        print("\n❌ Commands documented but not implemented:")
        for item in missing_implementations:
            print(f"  - {item}")
    
    if missing_documentation:
        print("\n❌ Commands implemented but not documented:")
        for item in missing_documentation:
            print(f"  - {item}")
    
    if alias_inconsistencies:
        print("\n❌ Commands with inconsistent aliases:")
        for item in alias_inconsistencies:
            print(f"  - {item}")
    
    return False

if __name__ == "__main__":
    success = validate_commands()
    sys.exit(0 if success else 1)
