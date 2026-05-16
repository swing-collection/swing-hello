# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
CLI Main Entry Point
====================

Main entry point for the Swing Hello command-line interface.

This module provides the ``main()`` function that serves as the CLI
entry point, parsing arguments and dispatching to appropriate commands.

Functions:
    main: Parse arguments and execute the requested command.

Example:
    From Python::

        from swing.hello.commands import main
        exit_code = main(['status'])

    As a module::

        $ python -m swing.hello status
        $ python -m swing.hello greet Alice --style formal
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
    Main CLI entry point.

    Parses command-line arguments and dispatches to the appropriate
    command handler. If no command is specified, defaults to showing
    the status.

    Args:
        args: Command-line arguments to parse. Defaults to ``sys.argv[1:]``
            when None.

    Returns:
        Exit code: 0 for success, non-zero for errors.

    Example:
        >>> main(['version'])
        swing-hello 0.3.0
        ...
        0

        >>> main(['greet', 'Alice'])
        Hello, Alice!
        0
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
