#!/usr/bin/env python3
"""Synchronize command aliases between commands-list.yml and pyproject.toml."""

import sys
import os
import re
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

def create_command_module(group_name, group_data):
    """Create a new command module file for a group."""
    print(f"📝 Creating command module for {group_name}...")
    
    module_path = Path(__file__).parent.parent / "src" / "starshipagentic" / "commands" / f"{group_name}_cmds.py"
    
    # Create template content
    template = f'''"""Commands for {group_data.get('description', 'the ' + group_name + ' group')}."""

import click
from rich.console import Console
from starshipagentic.utils.base_command import BaseCommand
from starshipagentic.utils.interactive import prompt_for_missing_param

console = Console()

# Create the command group
{group_name}_group = click.Group(
    name="{group_name.replace('_', '-')}",
    help="{group_data.get('description', 'Commands for the ' + group_name + ' group')}"
)

'''
    
    # Add commands
    for cmd_name, cmd_data in group_data.get('commands', {}).items():
        func_name = cmd_name.replace('-', '_')
        options = cmd_data.get('options', [])
        
        # Parse options
        option_lines = []
        param_names = []
        for option in options:
            if isinstance(option, str):
                # Parse option string like "--name: Description"
                parts = option.split(':', 1)
                opt_name = parts[0].strip().lstrip('-')
                opt_help = parts[1].strip() if len(parts) > 1 else ""
                option_lines.append(f'@click.option("--{opt_name}", help="{opt_help}")')
                param_names.append(opt_name)
        
        # Add command template
        template += f'''
@{group_name}_group.command(name="{cmd_name}")
{"".join(option_lines) if option_lines else ""}
def {func_name}({", ".join(param_names) if param_names else ""}):
    """{cmd_data.get('description', 'No description')}"""
    {f"""
    # Get parameter values using BaseCommand helper
    {' = '.join(param_names)} = BaseCommand.get_param_value(
        None, {param_names[0]}, "{param_names[0]}", "Enter {param_names[0]} for {cmd_name}"
    )
    """ if param_names else ""}
    click.echo(f"Executing {group_name} {cmd_name}")

'''
    
    # Add command functions for direct invocation
    template += "\n# Create command functions for direct invocation\n"
    for cmd_name in group_data.get('commands', {}):
        func_name = cmd_name.replace('-', '_')
        template += f'''
def {func_name}_command():
    """Wrapper for direct invocation of {func_name} command."""
    BaseCommand.parse_args_for_command({func_name})()
'''
    
    # Write the file
    with open(module_path, 'w') as f:
        f.write(template)
    
    print(f"✅ Created {module_path}")
    return True

def sync_cli_file():
    """Update cli.py to include all command groups from commands-list.yml."""
    print("🔄 Synchronizing CLI file...")
    
    # Load commands-list.yml
    commands_path = Path(__file__).parent.parent / "src" / "starshipagentic" / "commands-list.yml"
    with open(commands_path, 'r') as f:
        commands = yaml.safe_load(f)
    
    # Load cli.py
    cli_path = Path(__file__).parent.parent / "src" / "starshipagentic" / "cli.py"
    with open(cli_path, 'r') as f:
        cli_content = f.read()
    
    # Get all command groups
    group_names = list(commands.keys())
    
    # Check if each group has a module file
    for group_name in group_names:
        module_path = Path(__file__).parent.parent / "src" / "starshipagentic" / "commands" / f"{group_name}_cmds.py"
        if not module_path.exists():
            create_command_module(group_name, commands[group_name])
    
    # Update imports section
    import_pattern = r"from starshipagentic\.commands import \(\s*(.*?)\s*\)"
    import_match = re.search(import_pattern, cli_content, re.DOTALL)
    
    if import_match:
        current_imports = import_match.group(1)
        # Parse current imports
        import_lines = [line.strip() for line in current_imports.split(',')]
        import_lines = [line for line in import_lines if line]
        
        # Add missing imports
        added_imports = []
        for group_name in group_names:
            import_line = f"{group_name}_cmds"
            if import_line not in current_imports:
                import_lines.append(import_line)
                added_imports.append(group_name)
        
        # Sort imports
        import_lines.sort()
        
        # Format new imports section
        new_imports = ",\n    ".join(import_lines) + ","
        
        # Replace imports section
        new_import_section = f"from starshipagentic.commands import (\n    {new_imports}\n)"
        cli_content = re.sub(import_pattern, new_import_section, cli_content, flags=re.DOTALL)
        
        if added_imports:
            print(f"✅ Added imports for: {', '.join(added_imports)}")
    
    # Update GROUP_THEMES dictionary
    themes_pattern = r"GROUP_THEMES = \{(.*?)\}"
    themes_match = re.search(themes_pattern, cli_content, re.DOTALL)
    
    if themes_match:
        current_themes = themes_match.group(1)
        # Add missing themes
        added_themes = []
        for group_name in group_names:
            if f'"{group_name}"' not in current_themes:
                # Choose a color based on position in the list
                colors = ["blue", "green", "magenta", "cyan", "yellow", "bright_blue", 
                          "red", "bright_green", "bright_magenta", "bright_cyan", "bright_yellow"]
                color = colors[len(added_themes) % len(colors)]
                
                # Add to the end of the dictionary
                if current_themes.strip().endswith(","):
                    current_themes += f'\n    "{group_name}": "{color}",'
                else:
                    current_themes += f',\n    "{group_name}": "{color}",'
                
                added_themes.append(group_name)
        
        # Replace themes dictionary
        new_themes_section = f"GROUP_THEMES = {{{current_themes}}}"
        cli_content = re.sub(themes_pattern, new_themes_section, cli_content, flags=re.DOTALL)
        
        if added_themes:
            print(f"✅ Added themes for: {', '.join(added_themes)}")
    
    # Update GROUP_ICONS dictionary
    icons_pattern = r"GROUP_ICONS = \{(.*?)\}"
    icons_match = re.search(icons_pattern, cli_content, re.DOTALL)
    
    if icons_match:
        current_icons = icons_match.group(1)
        # Add missing icons
        added_icons = []
        for group_name in group_names:
            if f'"{group_name}"' not in current_icons:
                # Choose an icon
                icons = ["🚀", "📦", "🔧", "📊", "🔍", "📡", "🛠️", "📝", "🔬", "🧪", "🧭"]
                icon = icons[len(added_icons) % len(icons)]
                
                # Add to the end of the dictionary
                if current_icons.strip().endswith(","):
                    current_icons += f'\n    "{group_name}": "{icon}",'
                else:
                    current_icons += f',\n    "{group_name}": "{icon}",'
                
                added_icons.append(group_name)
        
        # Replace icons dictionary
        new_icons_section = f"GROUP_ICONS = {{{current_icons}}}"
        cli_content = re.sub(icons_pattern, new_icons_section, cli_content, flags=re.DOTALL)
        
        if added_icons:
            print(f"✅ Added icons for: {', '.join(added_icons)}")
    
    # Update enhance_group_help section
    enhance_pattern = r"# Enhance command groups with better help display\s*(.*?)# Add command groups"
    enhance_match = re.search(enhance_pattern, cli_content, re.DOTALL)
    
    if enhance_match:
        current_enhance = enhance_match.group(1)
        # Add missing enhance lines
        added_enhance = []
        for group_name in group_names:
            enhance_line = f"{group_name}_group = enhance_group_help({group_name}_cmds.{group_name}_group, \"{group_name}\")"
            if enhance_line not in current_enhance:
                if current_enhance.strip().endswith("\n"):
                    current_enhance += enhance_line + "\n"
                else:
                    current_enhance += "\n" + enhance_line + "\n"
                added_enhance.append(group_name)
        
        # Replace enhance section
        new_enhance_section = f"# Enhance command groups with better help display\n{current_enhance}\n# Add command groups"
        cli_content = re.sub(enhance_pattern, new_enhance_section, cli_content, flags=re.DOTALL)
        
        if added_enhance:
            print(f"✅ Added enhance_group_help for: {', '.join(added_enhance)}")
    
    # Update add_command section
    add_pattern = r"# Add command groups\s*(.*?)if __name__ == \"__main__\":"
    add_match = re.search(add_pattern, cli_content, re.DOTALL)
    
    if add_match:
        current_add = add_match.group(1)
        # Add missing add lines
        added_commands = []
        for group_name in group_names:
            add_line = f"main.add_command({group_name}_group, \"{group_name}\")"
            if add_line not in current_add:
                if current_add.strip().endswith("\n"):
                    current_add += add_line + "\n"
                else:
                    current_add += "\n" + add_line + "\n"
                added_commands.append(group_name)
        
        # Replace add section
        new_add_section = f"# Add command groups\n{current_add}\nif __name__ == \"__main__\":"
        cli_content = re.sub(add_pattern, new_add_section, cli_content, flags=re.DOTALL)
        
        if added_commands:
            print(f"✅ Added command registration for: {', '.join(added_commands)}")
    
    # Write updated cli.py
    with open(cli_path, 'w') as f:
        f.write(cli_content)
    
    if added_imports or added_themes or added_icons or added_enhance or added_commands:
        print("✅ Updated cli.py with new command groups")
    else:
        print("✅ No changes needed in cli.py")
    
    return True

def fix_command_imports():
    """Fix import statements in all command modules."""
    print("🔄 Fixing import statements in command modules...")
    
    # Get all command module files
    commands_dir = Path(__file__).parent.parent / "src" / "starshipagentic" / "commands"
    command_files = list(commands_dir.glob("*_cmds.py"))
    
    fixed_files = []
    for file_path in command_files:
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Check for incorrect imports
        has_changes = False
        
        # Fix src.starshipagentic imports
        if "from src.starshipagentic" in content:
            content = content.replace("from src.starshipagentic", "from starshipagentic")
            has_changes = True
        
        # Add missing BaseCommand import if needed
        if "BaseCommand" in content and "from starshipagentic.utils.base_command import BaseCommand" not in content:
            # Find the import section
            import_section_end = content.find("\n\n", content.find("import"))
            if import_section_end > 0:
                new_import = "\nfrom starshipagentic.utils.base_command import BaseCommand"
                content = content[:import_section_end] + new_import + content[import_section_end:]
                has_changes = True
        
        # Add missing interactive import if needed
        if "prompt_for_missing_param" in content and "from starshipagentic.utils.interactive import prompt_for_missing_param" not in content:
            import_section_end = content.find("\n\n", content.find("import"))
            if import_section_end > 0:
                new_import = "\nfrom starshipagentic.utils.interactive import prompt_for_missing_param"
                content = content[:import_section_end] + new_import + content[import_section_end:]
                has_changes = True
        
        # Add rich.console import if needed
        if "console.print" in content and "from rich.console import Console" not in content:
            import_section_end = content.find("\n\n", content.find("import"))
            if import_section_end > 0:
                new_import = "\nfrom rich.console import Console"
                content = content[:import_section_end] + new_import + content[import_section_end:]
                has_changes = True
                
                # Also add console initialization if missing
                if "console = Console()" not in content:
                    group_def_pos = content.find("def ") 
                    if group_def_pos > 0:
                        # Insert before the first function definition
                        content = content[:group_def_pos] + "\nconsole = Console()\n\n" + content[group_def_pos:]
                
        # Write changes back to file
        if has_changes:
            with open(file_path, 'w') as f:
                f.write(content)
            fixed_files.append(file_path.name)
    
    if fixed_files:
        print(f"✅ Fixed imports in {len(fixed_files)} files: {', '.join(fixed_files)}")
    else:
        print("✅ No import fixes needed")
    
    return True

def sync_aliases():
    """Synchronize aliases between commands-list.yml and pyproject.toml."""
    print("🔄 Synchronizing command aliases...")
    
    # First, sync the CLI file to ensure all command groups are registered
    sync_cli_file()
    
    # Fix imports in command modules
    fix_command_imports()
    
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
    changes_made = False
    
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
        changes_made = True
    else:
        print("✅ No changes needed in pyproject.toml")
    
    # Update commands-list.yml if we added aliases to it
    if updated_aliases:
        with open(commands_path, 'w') as f:
            yaml.dump(commands, f, sort_keys=False, default_flow_style=False)
        print(f"✅ Updated commands-list.yml with {len(updated_aliases)} aliases")
        changes_made = True
    
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
    
    # Install the package in development mode if changes were made
    if changes_made:
        print("\n🔄 Installing package in development mode...")
        import subprocess
        try:
            result = subprocess.run(
                ["pip", "install", "-e", "."], 
                cwd=Path(__file__).parent.parent,
                capture_output=True,
                text=True,
                check=True
            )
            print("✅ Package installed successfully")
            if result.stdout.strip():
                print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"❌ Error installing package: {e}")
            print(e.stdout)
            print(e.stderr)
    
    return True

def fix_specific_command_file(file_path):
    """Fix a specific command file by path."""
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return False
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Check for incorrect imports
    has_changes = False
    
    # Fix src.starshipagentic imports
    if "from src.starshipagentic" in content:
        content = content.replace("from src.starshipagentic", "from starshipagentic")
        has_changes = True
    
    # Add missing BaseCommand import if needed
    if "BaseCommand" in content and "from starshipagentic.utils.base_command import BaseCommand" not in content:
        # Find the import section
        import_section_end = content.find("\n\n", content.find("import"))
        if import_section_end > 0:
            new_import = "\nfrom starshipagentic.utils.base_command import BaseCommand"
            content = content[:import_section_end] + new_import + content[import_section_end:]
            has_changes = True
    
    # Write changes back to file
    if has_changes:
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"✅ Fixed imports in {os.path.basename(file_path)}")
    else:
        print(f"✅ No import fixes needed in {os.path.basename(file_path)}")
    
    return True

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Synchronize command aliases and fix imports")
    parser.add_argument("--fix-file", help="Fix imports in a specific command file")
    args = parser.parse_args()
    
    if args.fix_file:
        success = fix_specific_command_file(args.fix_file)
    else:
        success = sync_aliases()
    
    sys.exit(0 if success else 1)
