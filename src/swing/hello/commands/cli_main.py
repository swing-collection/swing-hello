# -*- coding: utf-8 -*-

"""
CLI Main
========

Main entry point for the Swing Hello CLI.
"""

# Import | Standard Library
from typing import Sequence

# Import | Local
from .cli_parser import create_parser
from .command_check import CheckCommand
from .command_greet import GreetCommand
from .command_status import StatusCommand
from .command_version import VersionCommand


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
    if parsed.command == "version":
        return VersionCommand().run()
    if parsed.command == "check":
        return CheckCommand().run()
    if parsed.command == "greet":
        return GreetCommand(
            name=parsed.name,
            style=parsed.style,
        ).run()
    parser.print_help()
    return 0


__all__: list[str] = ["main"]
