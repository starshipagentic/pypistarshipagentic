"""Main entry point for running starshipagentic as a module."""

import sys
import os
import click
from .cli import main
from .utils.command_registry import CommandRegistry

def preprocess_command_args():
    """
    Preprocess command arguments to handle shortened forms:
    1. 'starshipagentic probe map-planet' (fully qualified, no change needed)
    2. 'probe map-planet' (group shortcut)
    3. 'map-planet' (direct command)
    
    Note: For direct commands (case 3), the actual execution is handled by the entry point
    in pyproject.toml, which maps directly to the command function.
    """
    # Get command registry
    command_registry = CommandRegistry()
    
    # Get all group names and command names
    group_names = command_registry.get_all_groups()
    all_commands = {}
    for group in group_names:
        for cmd in command_registry.get_all_commands(group):
            all_commands[cmd['name']] = group
    
    # Get the script name
    script_name = os.path.basename(sys.argv[0])
    
    # Case 1: Script is a group name (e.g., 'probe map-planet')
    if script_name in group_names:
        # Adjust arguments to include the app name
        sys.argv = ['starshipagentic', script_name] + sys.argv[1:]
        return
    
    # Case 2: Normal invocation with group, ensure program name is correct
    if len(sys.argv) > 1 and sys.argv[1] in group_names:
        sys.argv[0] = 'starshipagentic'
        
    # Note: We don't need to handle Case 3 (direct command) here anymore
    # as it's handled by the entry point in pyproject.toml

if __name__ == "__main__":
    # Preprocess command arguments to handle shortened forms
    preprocess_command_args()
    
    # Pass command line arguments to the main CLI function
    sys.exit(main())
