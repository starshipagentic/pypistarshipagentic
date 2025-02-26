# Starship Agentic

A command-line toolkit for AI-assisted software development using a Star Trek-inspired interface.

## Why Starship Agentic?

Starship Agentic transforms the software development process into an engaging, Star Trek-inspired journey. It combines:

- **AI-powered development** - Leverage LLMs to generate, test, and fix code automatically
- **Guided workflow** - Follow a structured process from project initialization to deployment
- **Intuitive interface** - Use familiar Star Trek terminology for development tasks
- **Automated testing** - Run BDD and unit tests with AI-assisted error correction
- **Project management** - Track progress and maintain code quality throughout development

Whether you're building a new application or maintaining existing code, Starship Agentic helps you navigate the development universe more efficiently.

## Installation

```bash
pip install starshipagentic
```

## Requirements

- Python 3.8 or higher
- Git
- Internet connection (for AI-assisted features)
- API keys for specific LLM services (optional)

## Command Overview

Starship Agentic provides a suite of commands for managing your development workflow, organized into themed command groups.

### Main Command Structure

```
starshipagentic <command-group> <command> [options]
```

Each command is also available as a direct alias:

```
<command-alias> [options]
```

You can also simply run:

```
starshipagentic
```

Without any arguments to start the guided process from the beginning, which will help you navigate through the available commands.

## Command Groups

### Vessel Commands (`vessel_cmds.py`)
Initialize and select project templates.

| Command | Alias | Description |
|---------|-------|-------------|
| `tour-ship` | `tour` | Browse available ship templates/frameworks |
| `commission-ship` | `commission` | Clone template and run initialization |

### Mission Commands (`mission_cmds.py`)
Define and expand project requirements.

| Command | Alias | Description |
|---------|-------|-------------|
| `mission-brief` | `mission` | Generate initial project documentation |
| `expand-mission` | `expand` | Elaborate on project requirements |

### Architecture Commands (`architecture_cmds.py`)
Review and configure system architecture.

| Command | Alias | Description |
|---------|-------|-------------|
| `review-schematics` | `schematics` | Review state diagrams and DDD docs |
| `calibrate-technology` | `calibrate` | Configure tech stack settings |

### Navigation Commands (`navigation_cmds.py`)
Plan feature implementation.

| Command | Alias | Description |
|---------|-------|-------------|
| `plot-navigation` | `navigation` | Generate and review BDD Gherkin features |
| `set-waypoints` | `waypoints` | Create prioritized feature implementation plan |

### Transmission Commands (`transmission_cmds.py`)
Manage external data and API connections.

| Command | Alias | Description |
|---------|-------|-------------|
| `authorize-codes` | `authorize` | Configure API keys and service credentials |
| `scan-sector` | `scan` | Search for relevant topic URLs |
| `receive-transmission` | `transmission` | Scrape or input information from URLs |

### Exploration Commands (`exploration_cmds.py`)
Execute and test your implementation.

| Command | Alias | Description |
|---------|-------|-------------|
| `warp-speed` | `warp` | Run BDD tests with AI fixing loop |
| `trycoder` | - | Run unit tests with AI fixing loop |
| `engage` | - | Run complete test-fix cycles for all waypoints |

### Weapons Commands (`weapons_cmds.py`)
Remove problematic code and tests.

| Command | Alias | Description |
|---------|-------|-------------|
| `fire-photons` | `photons` | Remove problematic test steps |
| `aim-lasers` | `lasers` | Remove problematic code sections |
| `shields-up` | `shields` | Placeholder for defensive operations |

### Engineering Commands (`engineering_cmds.py`)
Manage project state and analyze code quality.

| Command | Alias | Description |
|---------|-------|-------------|
| `create-checkpoint` | `checkpoint` | Save project state |
| `restore-checkpoint` | `restore` | Roll back to saved state |
| `inspect-vessel` | `inspect` | Run framework-specific integrity checks |
| `complexity-report` | `complexity` | Generate code complexity metrics |

### Cosmic Commands (`cosmic_cmds.py`)
Special operations.

| Command | Alias | Description |
|---------|-------|-------------|
| `supernova` | - | Clean up Git repositories and metadata |

### Git Commands (`git_cmds.py`)
Git-related operations.

| Command | Alias | Description |
|---------|-------|-------------|
| `teleport` | - | Create new Git repo from code sections |

### MCARS Commands (`mcars_cmds.py`)
Code repository and search system.

| Command | Alias | Description |
|---------|-------|-------------|
| `search` | - | Search code repository database |
| `transport` | - | Store code snippets with AI-generated summaries |

## Examples

```bash
# Start the guided process
starshipagentic

# Browse available project templates
starshipagentic vessel tour-ship
# or simply
tour

# Initialize a new project
commission --template django

# Generate BDD features
navigation

# Run tests with AI fixing
warp --iterations 3

# Create a project checkpoint
checkpoint --message "Completed user authentication"

# Generate code complexity report
complexity
```

## Development

To contribute to Starship Agentic:

```bash
git clone https://github.com/yourusername/starshipagentic.git
cd starshipagentic
pip install -e .
```

## Roadmap

Future features planned for Starship Agentic:

- **Universal Translator** - Convert code between different programming languages
- **Holodeck** - Interactive visualization of project architecture and dependencies
- **Prime Directive** - Automated code quality enforcement and best practices
- **Replicator** - Generate boilerplate code for common patterns
- **Away Team** - Collaborative development features for team projects
- **Temporal Mechanics** - Advanced project versioning and branching strategies
- **Federation Integration** - Connect with additional AI services and development tools

## License

MIT
