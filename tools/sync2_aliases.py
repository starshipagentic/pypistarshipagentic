#!/usr/bin/env python3
"""
Starship Agentic Sync2 Tool

This tool reads commands-list.yml (the master data) and for each command under each group,
it ensures that a corresponding command package exists under:
    src/starshipagentic/commands/<group>/<command>/
If a package is missing, it scaffolds a new package with the following files (if not present):
  - __init__.py: Contains an auto-generated __all__ with the command function.
  - cli.py: A Click wrapper exposing <command>_command for CLI usage.
  - services.py: A stub file for the business logic of the command.
It also updates:
  - The __init__.py in each group folder to import all command packages.
  - The top-level commands/__init__.py to import all group folders.
  - The pyproject.toml [project.scripts] section with the expected aliases.
  - The main CLI (src/starshipagentic/cli.py) with auto-generated import lines.
The tool is generative – it creates missing files using fixed templates, but if files already exist,
it leaves any existing user logic intact (only updating __init__ files, etc).
"""

import os
import sys
import re
from pathlib import Path
import yaml
import tomli
import tomli_w
import subprocess

# Define key paths
BASE_DIR = Path(__file__).parent.parent
COMMANDS_LIST_PATH = BASE_DIR / "src" / "starshipagentic" / "commands-list.yml"
COMMANDS_DIR = BASE_DIR / "src" / "starshipagentic" / "commands"
PYPROJECT_PATH = BASE_DIR / "pyproject.toml"
CLI_PATH = BASE_DIR / "src" / "starshipagentic" / "cli.py"

# Templates for new command package files
INIT_TEMPLATE = '''"""Auto-generated __init__.py for the {command} command package."""

__all__ = ["{command}_command"]
'''
CLI_TEMPLATE = '''import click
from .services import {command}_service

@click.command()
@click.argument("input", required=False)
def {command}_command(input=None):
    """
    Auto-generated CLI command for {command}.
    """
    result = {command}_service(input)
    click.echo(result)

if __name__ == "__main__":
    {command}_command()
'''
SERVICES_TEMPLATE = '''def {command}_service(input):
    """
    Auto-generated service logic for {command}.
    Replace this stub with actual business logic.
    """
    return "Executed {command} with input: " + str(input)
'''

def load_commands_list():
    with open(COMMANDS_LIST_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def scaffold_command_package(group, command):
    """
    Ensure that the command package exists under:
        COMMANDS_DIR / group / sanitized_command
    Create __init__.py, cli.py, and services.py using templates if they do not exist.
    """
    sanitized_command = command.replace("-", "_")
    package_dir = COMMANDS_DIR / group / sanitized_command
    if not package_dir.exists():
        os.makedirs(package_dir)
        print(f"Created package directory: {package_dir}")

    # __init__.py: Only scaffold if it doesn't exist.
    init_file = package_dir / "__init__.py"
    if not init_file.exists():
        with open(init_file, "w", encoding="utf-8") as f:
            f.write(INIT_TEMPLATE.format(command=sanitized_command))
        print(f"Created: {init_file}")

    # cli.py: Scaffold if file does not exist.
    cli_file = package_dir / "cli.py"
    if not cli_file.exists():
        with open(cli_file, "w", encoding="utf-8") as f:
            f.write(CLI_TEMPLATE.format(command=sanitized_command))
        print(f"Created: {cli_file}")

    # services.py: Scaffold if file does not exist.
    services_file = package_dir / "services.py"
    if not services_file.exists():
        with open(services_file, "w", encoding="utf-8") as f:
            f.write(SERVICES_TEMPLATE.format(command=sanitized_command))
        print(f"Created: {services_file}")

def update_group_init(group):
    """
    In the group folder (COMMANDS_DIR/group), update __init__.py to list all command packages and create a click group object.
    """
    group_dir = COMMANDS_DIR / group
    init_file = group_dir / "__init__.py"
    packages = []
    if group_dir.exists():
        for item in os.listdir(group_dir):
            item_path = group_dir / item
            if item_path.is_dir() and (item_path / "cli.py").exists():
                packages.append(item)
        packages.sort()
    content = f'"""Auto-generated __init__.py for the {group} group."""\n\n'
    content += "import click\n"
    content += f'{group}_group = click.Group(name="{group}")\n\n'
    content += "__all__ = [\n"
    for pkg in packages:
        content += f'    "{pkg}",\n'
    content += f'    "{group}_group"\n'
    content += ']\n\n'
    for pkg in packages:
        content += f"from . import {pkg}\n"
    content += f'''

def run_group():
    """Entry point for running the {group} command group directly."""
    import sys
    from starshipagentic.cli import main as cli_main
    sys.argv = ['starshipagentic', '{group}'] + sys.argv[1:]
    cli_main()
'''
    with open(init_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated group __init__.py: {init_file}")

def update_commands_init():
    """
    Update the top-level commands/__init__.py to list all groups.
    """
    init_file = COMMANDS_DIR / "__init__.py"
    groups = []
    for item in os.listdir(COMMANDS_DIR):
        item_path = COMMANDS_DIR / item
        if item_path.is_dir():
            groups.append(item)
    groups.sort()
    content = '"""Auto-generated __init__.py for command groups."""\n\n__all__ = [\n'
    for group in groups:
        content += f'    "{group}",\n'
    content += ']\n\n'
    for group in groups:
        content += f"from . import {group}\n"
    with open(init_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated top-level commands __init__.py: {init_file}")

def generate_expected_aliases(commands_data):
    """
    Build a dictionary of expected aliases.
    For each command in each group, the alias maps to:
       starshipagentic.commands.<group>.<command>.cli:<command>_command
    Also add each group shortcut mapping to a run_group function:
       e.g., group alias "weapons" -> starshipagentic.commands.weapons:run_group
    And always include the main alias:
       "starshipagentic" -> starshipagentic.cli:main
    """
    expected = {}
    # Group-level aliases
    for group in commands_data.keys():
        expected[group] = f"starshipagentic.commands.{group}:run_group"
    # Command-level aliases
    for group, data in commands_data.items():
        cmds = data.get("commands", {})
        for cmd in cmds.keys():
            sanitized_cmd = cmd.replace("-", "_")
            alias = cmd.replace("_", "-")
            expected[alias] = f"starshipagentic.commands.{group}.{sanitized_cmd}.cli:{sanitized_cmd}_command"
            # Also consider any additional aliases defined in commands-list.yml
            for extra_alias in cmds.get(cmd, {}).get("aliases", []):
                expected[extra_alias] = f"starshipagentic.commands.{group}.{sanitized_cmd}.cli:{sanitized_cmd}_command"
    # Main alias
    expected["starshipagentic"] = "starshipagentic.cli:main"
    return expected

def update_pyproject_scripts(expected_aliases):
    """
    Update the [project.scripts] section in pyproject.toml.
    """
    with open(PYPROJECT_PATH, "rb") as f:
        pyproject = tomli.load(f)
    scripts = pyproject.get("project", {}).get("scripts", {})
    added_aliases = []
    updated_aliases = []
    for alias, target in expected_aliases.items():
        if alias not in scripts:
            scripts[alias] = target
            added_aliases.append(f"{alias} -> {target}")
        elif scripts[alias] != target:
            old = scripts[alias]
            scripts[alias] = target
            updated_aliases.append(f"{alias}: {old} => {target}")
    pyproject.setdefault("project", {})["scripts"] = scripts
    with open(PYPROJECT_PATH, "wb") as f:
        tomli_w.dump(pyproject, f)
    if added_aliases or updated_aliases:
        print("Updated pyproject.toml scripts:")
        for a in added_aliases:
            print("  Added:", a)
        for u in updated_aliases:
            print("  Updated:", u)
    else:
        print("No changes needed in pyproject.toml scripts.")

def update_cli_main(expected_aliases):
    """
    Update the main CLI file (CLI_PATH) with auto-generated import lines within markers.
    """
    with open(CLI_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    start_marker = "# [AUTO-GENERATED COMMAND IMPORTS START]"
    end_marker = "# [AUTO-GENERATED COMMAND IMPORTS END]"
    generated = [start_marker]
    # Exclude main alias
    for alias, target in expected_aliases.items():
        if alias == "starshipagentic":
            continue
        module, func = target.split(":")
        generated.append(f"from {module} import {func}  # alias: {alias}")
    generated.append(end_marker)
    gen_block = "\n".join(generated)
    if start_marker in content and end_marker in content:
        content = re.sub(
            rf"{re.escape(start_marker)}.*?{re.escape(end_marker)}",
            gen_block,
            content,
            flags=re.DOTALL,
        )
    else:
        lines = content.splitlines()
        insert_at = 0
        if lines and lines[0].startswith("#!"):
            insert_at = 1
        lines.insert(insert_at, gen_block)
        content = "\n".join(lines)
    with open(CLI_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated main CLI file:", CLI_PATH)

def sync_cli_file():
    """
    Synchronize cli.py by ensuring that for each group in commands-list.yml,
    if the file for that group doesn't exist, scaffold a command module.
    Then update the import section in cli.py.
    """
    print("  ├─ Synchronizing CLI file...")
    commands_data = load_commands_list()
    group_names = list(commands_data.keys())
    print(f"  Debug: Found groups: {', '.join(group_names)}")
    for group in group_names:
        # Check if group folder exists; if not, create it.
        group_dir = COMMANDS_DIR / group
        if not group_dir.exists():
            os.makedirs(group_dir)
            print(f"Created group directory: {group_dir}")
        # For each command in the group, scaffold its package if missing.
        for cmd in commands_data[group].get("commands", {}):
            scaffold_command_package(group, cmd)
        update_group_init(group)
    update_commands_init()
    expected_aliases = generate_expected_aliases(commands_data)
    update_pyproject_scripts(expected_aliases)
    update_cli_main(expected_aliases)
    return True

def fix_command_imports():
    """
    Optionally, perform lightweight fixes on command package files (e.g. ensure proper imports).
    This function will not overwrite existing logic.
    """
    print("  ├─ Fixing imports in command packages (if needed)...")
    # (This function can be expanded as necessary.)
    return True

def sync_aliases():
    """
    Main synchronization function.
    It reads commands-list.yml, scaffolds missing command packages,
    updates group and top-level __init__.py files, pyproject.toml scripts,
    and updates the main CLI file.
    """
    print("🔄 Starting synchronization based on commands-list.yml...")
    sync_cli_file()
    fix_command_imports()
    print("Sync complete.")
    return True

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Synchronize command aliases and scaffold command packages")
    parser.add_argument("--fix-file", help="Fix imports in a specific command file")
    args = parser.parse_args()
    if args.fix_file:
        # Functionality for a specific file fix can be added here.
        print(f"Fixing file: {args.fix_file}")
    else:
        sync_aliases()

if __name__ == "__main__":
    main()
