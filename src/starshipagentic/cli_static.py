#!/usr/bin/env python3
"""
Static CLI definitions for Starship Agentic.
This file contains code that does not change dynamically.
"""

import click

def enhance_group_help(group_obj, group_name):
    """
    Enhance a command group with custom help formatting.
    Replace this stub with your actual enhancement implementation.
    """
    # Example stub: simply return the group object unchanged.
    return group_obj

main = click.Group()

# Import the auto-generated dynamic CLI code.
from . import cli_generated
