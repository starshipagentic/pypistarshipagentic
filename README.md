# Starship Agentic

**License Notice:** All source code in this repository is protected under the GNU Affero General Public License (AGPL) v3 or later. For full details, please refer to the LICENSE.md file. To help maintain legal clarity, consider adding the header from LICENSE_HEADER.txt to your source code files.

A command-line toolkit for AI-assisted software development using a sci-fi -inspired interface.

## Why Starship Agentic?

Starship Agentic transforms the software development process into an engaging, sci-fi inspired journey. It combines:

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

# Command Reference

## Vessel Commands

Initialize and select project templates

| Command | Alias | Description |
|---------|-------|-------------|
| `vessel tour-ship` | `tour` | Browse available ship templates/frameworks |
| `vessel commission-ship` | `commission` | Clone template and run initialization |
| `vessel visualize-ship` | `` | Launch a Pygame visualization of the specified ship |

## Mission Commands

Define and expand project requirements

| Command | Alias | Description |
|---------|-------|-------------|
| `mission mission-brief` | `mission` | Define project mission and requirements |
| `mission expand-mission` | `expand` | Expand existing requirements |

## Architecture Commands

Review and configure system architecture

| Command | Alias | Description |
|---------|-------|-------------|
| `architecture review-schematics` | `schematics` | Review system architecture diagrams (MD documents for state diagram and DDD) |
| `architecture calibrate-technology` | `calibrate` | Configure technology stack |

## Navigation Commands

Plan feature implementation

| Command | Alias | Description |
|---------|-------|-------------|
| `navigation plot-navigation` | `navigation` | Generate and review BDD gherkin feature files |
| `navigation set-waypoints` | `waypoints` | Create order for working on features (project plan checklist) |

## Transmission Commands

Manage external data and API connections

| Command | Alias | Description |
|---------|-------|-------------|
| `transmission authorize-codes` | `authorize` | Configure API credentials needed for features |
| `transmission scan-sector` | `scan` | Search for topic to find URLs for scraping |
| `transmission receive-transmission` | `transmission` | Scrape or directly input information from a known URL |

## Probe Commands

Generate initial code tracks and connect the top down BDD step coverage

| Command | Alias | Description |
|---------|-------|-------------|
| `probe map-planet` | `map` | Lightweight: create initial folder, and file names scaffolding, not the BDD steps yet |
| `probe build-landing-zone` | `buildlz` | Create initial code tracks within the files that map-planet created |
| `probe fabricate-infrastructure` | `fabricate` | Generate BDD steps to connect the code laid down in the landing zone |

## Exploration Commands

Execute and test your implementation

| Command | Alias | Description |
|---------|-------|-------------|
| `exploration warp-speed` | `warp` | Top-down BDD behave driven loop (get behave errors and feed to AI to fix) |
| `exploration trycoder` | `trycoder` | Bottom-up unit test driven loop (get errors and feed to AI to fix) |
| `exploration engage` | `engage` | Run warp cycle and trycoder to repeat full set of waypoints N times |

## Weapons Commands

Remove problematic code and tests

| Command | Alias | Description |
|---------|-------|-------------|
| `weapons fire-photons` | `photons` | Remove specified steps that are causing trouble |
| `weapons aim-lasers` | `lasers` | Remove specified code that is causing trouble |
| `weapons shields-up` | `shields` | Protect code from changes (placeholder) |

## Engineering Commands

Manage project state and analyze code quality

| Command | Alias | Description |
|---------|-------|-------------|
| `engineering create-checkpoint` | `checkpoint` | Create a copy of entire folder and/or git tags |
| `engineering restore-checkpoint` | `restore` | Roll code back to checkpoint (git or folder copy) |
| `engineering inspect-vessel` | `inspect` | Run framework-specific checks to report on integrity |
| `engineering complexity-report` | `complexity` | Run radon mi and radon cc to report on code complexity issues |

## Cosmic Commands

Special operations

| Command | Alias | Description |
|---------|-------|-------------|
| `cosmic supernova` | `supernova` | Remove all git stuff (searches through all sub-folders) |

## Beam Commands

Git-related operations

| Command | Alias | Description |
|---------|-------|-------------|
| `beam teleport` | `teleport` | Take pieces of code and make a new git repo almost automatically |

## Mcars Commands

Code repository and search system

| Command | Alias | Description |
|---------|-------|-------------|
| `mcars search` | `search` | Search for code in the MCARS database |
| `mcars transport` | `transport` | Store pointers/copies of code with AI-generated summaries in tinydb |

## Droid Commands

Explanation and assistance commands

| Command | Alias | Description |
|---------|-------|-------------|
| `droid droid-splain` | `droid` | Get explanation from droid assistant |
| `droid man-splain` | `splain` | Get manual page for a topic |


## Examples

```bash
# Start the guided process
starshipagentic

# Browse available project templates
starshipagentic vessel tour-ship
# or simply
tour

# Initialize a new project (three equivalent ways)
commission django-galaxy
# or with named parameters
commission --template django-galaxy --name myproject
# or interactively (will prompt for missing information)
commission

# Generate BDD features
navigation
# or with parameters
navigation gherkin

# Run tests with AI fixing
warp 3  # shorthand for 3 iterations
# or with named parameters
warp --iterations 3

# Create a project checkpoint
checkpoint "Completed user authentication"
# or with named parameters
checkpoint --message "Completed user authentication"
# or interactively
checkpoint

# Generate code complexity report
complexity
# or with threshold parameter
complexity 15
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
