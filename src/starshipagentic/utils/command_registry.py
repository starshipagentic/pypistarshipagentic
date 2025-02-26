"""Command registry for Starship Agentic."""

import yaml
from pathlib import Path

class CommandRegistry:
    _instance = None
    _commands = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CommandRegistry, cls).__new__(cls)
            cls._instance._load_commands()
        return cls._instance
    
    def _load_commands(self):
        """Load commands from YAML file."""
        commands_path = Path(__file__).parent.parent / "commands-list.yml"
        with open(commands_path, 'r') as f:
            self._commands = yaml.safe_load(f)
    
    def get_all_groups(self):
        """Return all command groups."""
        return self._commands.keys()
    
    def get_group_info(self, group_name):
        """Return info for a specific command group."""
        return self._commands.get(group_name, {})
    
    def get_command_info(self, group_name, command_name):
        """Return info for a specific command."""
        group = self.get_group_info(group_name)
        return group.get('commands', {}).get(command_name, {})
    
    def get_all_commands(self, group_name=None):
        """Return all commands, optionally filtered by group."""
        if group_name:
            group = self.get_group_info(group_name)
            return group.get('commands', {})
        
        all_commands = {}
        for group_name, group_data in self._commands.items():
            for cmd_name, cmd_data in group_data.get('commands', {}).items():
                all_commands[f"{group_name} {cmd_name}"] = cmd_data
        return all_commands
    
    def get_aliases_map(self):
        """Return a mapping of aliases to their full commands."""
        aliases_map = {}
        for group_name, group_data in self._commands.items():
            for cmd_name, cmd_data in group_data.get('commands', {}).items():
                for alias in cmd_data.get('aliases', []):
                    aliases_map[alias] = (group_name, cmd_name)
        return aliases_map
    
    def get_example_command(self, group_name):
        """Return an example command for a group."""
        group = self.get_group_info(group_name)
        commands = group.get('commands', {})
        if not commands:
            return f"{group_name}"
        
        # Get first command as example
        cmd_name = next(iter(commands.keys()), "")
        return f"{group_name} {cmd_name}"
    
    def validate_commands(self):
        """Validate that all commands in YAML have implementations."""
        # This would check that all commands in YAML have corresponding
        # implementations in the codebase. For now, it's a placeholder.
        return True

# Create a singleton instance
command_registry = CommandRegistry()
