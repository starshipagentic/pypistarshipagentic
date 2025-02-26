# Starship Agentic System Knowledge

This document contains important technical details about how the Starship Agentic CLI works.

## Command Aliases Implementation

The Starship Agentic CLI uses a unique approach to implement command aliases:

### How Aliases Work

1. **Entry Points in pyproject.toml**:
   - Aliases are implemented as separate executable entry points in `pyproject.toml`
   - Each alias is a direct script that calls the corresponding command function
   - Example: `mission = "starshipagentic.commands.mission_cmds:mission_brief_command"`

2. **Base Command Wrapper**:
   - The `BaseCommand.parse_args_for_command()` function creates wrappers for direct command invocation
   - These wrappers allow commands to be run directly without going through the Click command structure
   - Example: `mission_brief_command = base_cmd.parse_args_for_command(mission_brief)`

3. **Documentation in commands-list.yml**:
   - The `commands-list.yml` file documents the relationships between commands and their aliases
   - This is for documentation purposes only and doesn't affect functionality

### Important Notes

- Aliases are NOT implemented using Click's command resolution
- When you run an alias (e.g., `mission`), you're executing a separate script, not using Click's command structure
- The main CLI (`starshipagentic`) uses Click's standard command groups and commands
- Do NOT use `aliases=[]` parameter in Click command decorators - Click doesn't support this

### Example

When you run:
- `mission` - You're executing the script defined by the entry point, which calls `mission_brief_command`
- `starshipagentic mission` - You're using Click to execute the `mission` command group

## Command Structure

The CLI has a two-level command structure:
1. Command groups (e.g., `vessel`, `mission`, `architecture`)
2. Commands within each group (e.g., `tour-ship`, `mission-brief`)

Each command has:
- A long-form name used in the Click command structure
- Potentially a short-form alias as a separate entry point
- Documentation in the commands-list.yml file

## Implementation Details

- The `BaseCommand` class provides utilities for command implementation
- The `interactive.py` module handles interactive prompts
- Rich formatting is used for all console output
- YAML configuration files control command sequences

## Interactive Prompts

The `interactive.py` module provides utilities for interactive command-line prompts:

- `prompt_for_missing_param()` - Prompts the user for a parameter value if not provided
- `confirm_action()` - Asks for confirmation before proceeding with an action

These functions handle test environments gracefully by returning default values when running under pytest.

## Command Execution Flow

1. User runs a command (either through the main CLI or a direct alias)
2. Command function is called with arguments from the command line
3. Missing parameters are prompted for using the interactive module
4. Command executes its logic
5. Results are displayed using rich formatting

## Configuration

- Configuration is loaded from YAML files in various locations
- Command sequences can be defined in the configuration
- The CLI checks multiple locations for configuration files
