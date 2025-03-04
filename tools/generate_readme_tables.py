#!/usr/bin/env python3
# Starship Agentic License Header
#
# Copyright (c) 2025 Travis Somerville and David Samson
#
# This file is part of Starship Agentic.
#
# It is licensed under the GNU Affero General Public License (AGPL) v3 or later.
# For full details, see the LICENSE.md file in the project root.
"""Generate command tables for README.md from commands-list.yml."""

import sys
import os
from pathlib import Path
import yaml

# Add the project root to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.starshipagentic.utils.command_registry import command_registry

def generate_command_tables():
    """Generate markdown tables for README.md from commands-list.yml."""
    # Generate markdown
    markdown = "# Command Reference\n\n"
    
    for group_name in command_registry.get_all_groups():
        group_info = command_registry.get_group_info(group_name)
        
        markdown += f"## {group_name.capitalize()} Commands\n\n"
        markdown += f"{group_info.get('description', '')}\n\n"
        
        # Create table header
        markdown += "| Command | Alias | Description |\n"
        markdown += "|---------|-------|-------------|\n"
        
        # Add each command
        commands = group_info.get('commands', {})
        for cmd_name, cmd_data in commands.items():
            aliases = ", ".join(cmd_data.get('aliases', []))
            description = cmd_data.get('description', 'No description')
            markdown += f"| `{group_name} {cmd_name}` | `{aliases}` | {description} |\n"
        
        markdown += "\n"
    
    return markdown

def update_readme_section(readme_path, section_content, start_marker, end_marker):
    """Update a section in the README.md file."""
    if not readme_path.exists():
        print(f"README file not found: {readme_path}")
        return False
    
    with open(readme_path, 'r') as f:
        content = f.read()
    
    # Find the section to replace
    start_index = content.find(start_marker)
    end_index = content.find(end_marker)
    
    if start_index == -1 or end_index == -1:
        print(f"Section markers not found in README: {start_marker}, {end_marker}")
        return False
    
    # Replace the section
    new_content = (
        content[:start_index + len(start_marker)] + 
        "\n\n" + section_content + "\n" + 
        content[end_index:]
    )
    
    with open(readme_path, 'w') as f:
        f.write(new_content)
    
    return True

if __name__ == "__main__":
    # Generate the command tables
    tables = generate_command_tables()
    
    # Define the README path and section markers
    readme_path = Path(__file__).parent.parent / "README.md"
    start_marker = "## Command Groups"
    end_marker = "## Examples"
    
    if len(sys.argv) > 1 and sys.argv[1] == "--print":
        # Just print the tables to stdout
        print(tables)
    else:
        # Update the README file
        success = update_readme_section(readme_path, tables, start_marker, end_marker)
        if success:
            print(f"Successfully updated command tables in {readme_path}")
        else:
            print(f"Failed to update command tables in {readme_path}")
            print("Generated tables:")
            print(tables)
