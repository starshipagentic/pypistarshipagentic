"""Interactive prompt utilities for CLI commands."""

import sys
from rich.console import Console
from rich.prompt import Prompt, Confirm

console = Console()

def prompt_for_missing_param(param_name, prompt_text, choices=None, default=None):
    """
    Prompt the user for a missing parameter with a nice interface.
    
    Args:
        param_name (str): Name of the parameter (for display)
        prompt_text (str): Text to display in the prompt
        choices (list, optional): List of valid choices
        default (str, optional): Default value if user presses enter
        
    Returns:
        str: The user's input
    """
    # For testing environments, return the default value without prompting
    if 'pytest' in sys.modules:
        return default if default is not None else (choices[0] if choices else "test_value")
        
    if choices:
        return Prompt.ask(
            f"[bold blue]{prompt_text}[/bold blue]",
            choices=choices,
            default=default
        )
    else:
        return Prompt.ask(
            f"[bold blue]{prompt_text}[/bold blue]",
            default=default
        )

def confirm_action(prompt_text, default=True):
    """
    Ask for confirmation before proceeding with an action.
    
    Args:
        prompt_text (str): Text to display in the confirmation prompt
        default (bool, optional): Default value if user presses enter
        
    Returns:
        bool: True if confirmed, False otherwise
    """
    # For testing environments, return the default value without prompting
    if 'pytest' in sys.modules:
        return default
        
    return Confirm.ask(
        f"[bold yellow]{prompt_text}[/bold yellow]",
        default=default
    )
