"""Base command class for all Starship Agentic commands."""

import sys
import click
from rich.console import Console
from .interactive import prompt_for_missing_param, confirm_action

console = Console()

class BaseCommand:
    """Base class for all Starship Agentic commands."""
    
    @staticmethod
    def get_param_value(arg_value, opt_value, param_name, prompt_text, choices=None, default=None):
        """
        Get parameter value from argument, option, or interactive prompt.
        
        Args:
            arg_value: Value from positional argument
            opt_value: Value from named option
            param_name: Name of the parameter
            prompt_text: Text to display in the prompt
            choices: List of valid choices
            default: Default value
            
        Returns:
            The parameter value
        """
        # Use the option value if provided, otherwise use the argument
        value = opt_value or arg_value
        
        # If value is not provided, prompt for it
        if value is None:
            value = prompt_for_missing_param(
                param_name,
                prompt_text,
                choices=choices,
                default=default
            )
            
        return value
    
    @staticmethod
    def parse_args_for_command(command_func):
        """
        Create a wrapper that parses sys.argv for direct command invocation.
        
        Args:
            command_func: The Click command function to wrap
            
        Returns:
            A function that parses sys.argv and calls the command
        """
        def wrapper():
            """Parse sys.argv and call the command function."""
            # Extract positional arguments
            args = {}
            options = {}
            
            # Get parameter names from the command function
            params = getattr(command_func, '__click_params__', [])
            arg_names = [p.name for p in params if isinstance(p, click.Argument)]
            option_names = [p.name for p in params if isinstance(p, click.Option)]
            
            # Extract positional arguments from sys.argv
            for i, arg_name in enumerate(arg_names):
                if i + 1 < len(sys.argv):
                    # Skip arguments that look like options (start with -)
                    if not sys.argv[i + 1].startswith('-'):
                        args[arg_name] = sys.argv[i + 1]
            
            # Extract options from sys.argv
            i = 1
            while i < len(sys.argv):
                arg = sys.argv[i]
                if arg.startswith('--'):
                    opt_name = arg[2:]
                    if opt_name in option_names:
                        if i + 1 < len(sys.argv) and not sys.argv[i + 1].startswith('-'):
                            options[opt_name] = sys.argv[i + 1]
                            i += 2
                        else:
                            # Boolean flag
                            options[opt_name] = True
                            i += 1
                    else:
                        i += 1
                elif arg.startswith('-'):
                    # Short options
                    i += 1
                else:
                    i += 1
            
            # Call the command function with extracted arguments
            kwargs = {}
            for name in arg_names:
                kwargs[name] = args.get(name)
            for name in option_names:
                if name in options:
                    kwargs[name] = options[name]
            
            return command_func(**kwargs)
        
        return wrapper
