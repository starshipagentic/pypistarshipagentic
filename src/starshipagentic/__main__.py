"""Main entry point for running starshipagentic as a module."""

import sys
import click
from .cli import main

if __name__ == "__main__":
    # Pass command line arguments to the main CLI function
    sys.exit(main())
