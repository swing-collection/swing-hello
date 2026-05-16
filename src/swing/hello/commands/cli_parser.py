# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
CLI Argument Parser
===================

Command-line argument parser configuration for the Swing Hello application.

This module creates and configures an ``argparse.ArgumentParser`` with
subcommands for various CLI operations.

Functions:
    create_parser: Create and configure the argument parser.

Subcommands:
    status: Check application status.
    version: Display version information.
    check: Run Django system checks.
    greet: Generate a greeting (takes name and optional style).

Example:
    >>> parser = create_parser()
    >>> args = parser.parse_args(['greet', 'Alice', '--style', 'formal'])
    >>> args.name
    'Alice'
    >>> args.style
    'formal'
"""

# Import | Standard Library
import argparse


def create_parser() -> argparse.ArgumentParser:
    """
    Create and configure the CLI argument parser.

    Creates a parser with subcommands for status, version, check,
    and greet operations. The greet subcommand accepts a name
    argument and optional style flag.

    Returns:
        A configured ArgumentParser with all subcommands registered.

    Example:
        >>> parser = create_parser()
        >>> parser.parse_args(['status'])
        Namespace(command='status')

        >>> parser.parse_args(['greet', 'Bob'])
        Namespace(command='greet', name='Bob', style='casual')
    """
    parser = argparse.ArgumentParser(
        prog="swing-hello",
        description="Swing Hello CLI - A Django greeting application",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        title="commands",
        description="Available commands",
    )

    # Status command
    subparsers.add_parser(
        "status",
        help="Check application status",
    )

    # Version command
    subparsers.add_parser(
        "version",
        help="Display version information",
    )

    # Check command
    subparsers.add_parser(
        "check",
        help="Run Django system checks",
    )

    # Greet command
    greet_parser = subparsers.add_parser(
        "greet",
        help="Generate a greeting",
    )
    greet_parser.add_argument(
        "name",
        type=str,
        help="The name to greet",
    )
    greet_parser.add_argument(
        "-s",
        "--style",
        type=str,
        choices=["formal", "casual", "enthusiastic"],
        default="casual",
        help="Greeting style (default: casual)",
    )

    return parser


__all__: list[str] = ["create_parser"]
