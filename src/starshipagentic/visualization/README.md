# Starship Agentic Visualization

This module provides a graphical interface for Starship Agentic using Pygame.

## Features

- Visual representation of different starships
- Interactive buttons to trigger commands
- Command output display
- Themed interface with space aesthetics

## Usage

```bash
# Launch visualization for the Enterprise
starshipagentic vessel visualize-ship --ship enterprise

# Or use the direct command
visualize --ship voyager
```

## Requirements

This module requires Pygame:

```bash
pip install pygame
```

## Design

The visualization module is designed as a separate concern from the core command functionality. This means:

1. All core commands work without Pygame installed
2. The visualization is an optional enhancement
3. Commands can be triggered from both CLI and the visualization interface
