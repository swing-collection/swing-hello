# -*- coding: utf-8 -*-

"""
CLI Module
==========

Command-line interface for the Swing Hello application.
"""

# Import | Standard Library
import argparse
from typing import Sequence

# Import | Local
from .command_check import CheckCommand
from .command_greet import GreetCommand
from .command_status import StatusCommand
from .command_version import VersionCommand


def create_parser() -> argparse.ArgumentParser:
    """
    Create the argument parser for the CLI.

    Returns:
        argparse.ArgumentParser: The configured parser.
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


def main(args: Sequence[str] | None = None) -> int:
    """
    Main entry point for the CLI.

    Args:
        args: Command line arguments (defaults to sys.argv).

    Returns:
        int: Exit code.
    """
    parser = create_parser()
    parsed = parser.parse_args(args)

    if parsed.command == "status" or parsed.command is None:
        return StatusCommand().run()
    elif parsed.command == "version":
        return VersionCommand().run()
    elif parsed.command == "check":
        return CheckCommand().run()
    elif parsed.command == "greet":
        return GreetCommand(
            name=parsed.name,
            style=parsed.style,
        ).run()
    else:
        parser.print_help()
        return 0


__all__: list[str] = ["create_parser", "main"]
