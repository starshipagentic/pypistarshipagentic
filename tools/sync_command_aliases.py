#!/usr/bin/env python3
"""Synchronize command aliases between commands-list.yml and pyproject.toml."""

import sys
import os
from pathlib import Path
import yaml

# Add the project root to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    import tomli
    import tomli_w
except ImportError:
    print("This tool requires tomli and tomli_w packages.")
    print("Install them with: pip install tomli tomli-w")
    sys.exit(1)

def sync_aliases():
    """Synchronize aliases between commands-list.yml and pyproject.toml."""
    print("🔄 Synchronizing command aliases...")
    
    # Load commands-list.yml
    commands_path = Path(__file__).parent.parent / "src" / "starshipagentic" / "commands-list.yml"
    with open(commands_path, 'r') as f:
        commands = yaml.safe_load(f)
    
    # Load pyproject.toml
    pyproject_path = Path(__file__).parent.parent / "pyproject.toml"
    with open(pyproject_path, "rb") as f:
        pyproject = tomli.load(f)
    
    # Get current scripts from pyproject.toml
    scripts = pyproject.get("project", {}).get("scripts", {})
    
    # Keep track of changes
    added_aliases = []
    removed_aliases = []
    updated_aliases = []
    
    # Build a map of expected aliases from commands-list.yml
    expected_aliases = {}
    for group_name, group_data in commands.items():
        for cmd_name, cmd_data in group_data.get("commands", {}).items():
            cmd_func_name = cmd_name.replace("-", "_")
            target = f"starshipagentic.commands.{group_name}_cmds:{cmd_func_name}_command"
            
            for alias in cmd_data.get("aliases", []):
                expected_aliases[alias] = target
    
    # Add the main command (should always be present)
    expected_aliases["starshipagentic"] = "starshipagentic.cli:main"
    
    # Compare and update scripts
    for alias, target in expected_aliases.items():
        if alias not in scripts:
            scripts[alias] = target
            added_aliases.append(f"{alias} -> {target}")
        elif scripts[alias] != target:
            old_target = scripts[alias]
            scripts[alias] = target
            updated_aliases.append(f"{alias}: {old_target} -> {target}")
    
    # Check for aliases in pyproject.toml that aren't in commands-list.yml
    for alias, target in list(scripts.items()):
        if alias != "starshipagentic" and alias not in expected_aliases:
            # Try to find the command this alias points to
            try:
                module_path, func_name = target.split(":")
                group_name = module_path.split(".")[-1].replace("_cmds", "")
                cmd_func_name = func_name.replace("_command", "")
                cmd_name = cmd_func_name.replace("_", "-")
                
                # Check if this command exists in the registry
                if group_name in commands and cmd_name in commands[group_name].get('commands', {}):
                    # Add this alias to the command in commands-list.yml
                    if 'aliases' not in commands[group_name]['commands'][cmd_name]:
                        commands[group_name]['commands'][cmd_name]['aliases'] = []
                    
                    if alias not in commands[group_name]['commands'][cmd_name]['aliases']:
                        commands[group_name]['commands'][cmd_name]['aliases'].append(alias)
                        updated_aliases.append(f"{alias}: Added to {group_name} {cmd_name}")
                else:
                    # Don't automatically remove aliases, just report them
                    removed_aliases.append(f"{alias} -> {target}")
            except (ValueError, KeyError, IndexError):
                # Don't automatically remove aliases, just report them
                removed_aliases.append(f"{alias} -> {target}")
    
    # Update pyproject.toml if there were changes
    if added_aliases or updated_aliases:
        pyproject["project"]["scripts"] = scripts
        with open(pyproject_path, "wb") as f:
            tomli_w.dump(pyproject, f)
        print(f"✅ Updated pyproject.toml with {len(added_aliases)} new and {len(updated_aliases)} modified aliases")
    else:
        print("✅ No changes needed in pyproject.toml")
    
    # Update commands-list.yml if we added aliases to it
    if updated_aliases:
        with open(commands_path, 'w') as f:
            yaml.dump(commands, f, sort_keys=False, default_flow_style=False)
        print(f"✅ Updated commands-list.yml with {len(updated_aliases)} aliases")
    
    # Report changes
    if added_aliases:
        print("\nAdded aliases:")
        for alias in added_aliases:
            print(f"  + {alias}")
    
    if updated_aliases:
        print("\nUpdated aliases:")
        for alias in updated_aliases:
            print(f"  ~ {alias}")
    
    if removed_aliases:
        print("\nPotential aliases to remove (not automatically removed):")
        for alias in removed_aliases:
            print(f"  - {alias}")
    
    return True

if __name__ == "__main__":
    success = sync_aliases()
    sys.exit(0 if success else 1)
