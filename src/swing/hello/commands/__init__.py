# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Swing Hello Commands Module
===========================

Command-line interface utilities for the Swing Hello application.

This module provides a CLI for interacting with the application from
the terminal, including status checks, version info, system checks,
and greeting generation.

Classes
-------

- :class:`StatusCommand`: Check application status and configuration.
- :class:`VersionCommand`: Display version, author, and license info.
- :class:`CheckCommand`: Run Django system checks for this app.
- :class:`GreetCommand`: Generate a greeting from command line.

Functions
---------

- :func:`main`: CLI entry point.
- :func:`create_parser`: Create the argument parser.

Constants
---------

- ``VERSION``: Current application version.
- ``AUTHOR``: Package author name.
- ``LICENSE``: Package license.

Example:
    Command line usage::

        $ python -m swing.hello status
        $ python -m swing.hello version
        $ python -m swing.hello greet Alice --style formal

    Programmatic usage::

        from swing.hello.commands import StatusCommand, GreetCommand

        StatusCommand().run()
        GreetCommand(name='Alice', style='formal').run()
"""

# =============================================================================
# Imports
# =============================================================================


# Import | Local
# Import | Local Modules
from .cli_main import main
from .cli_parser import create_parser
from .command_check import CheckCommand
from .command_greet import GreetCommand
from .command_status import StatusCommand
from .command_version import VersionCommand
from .constants import AUTHOR, LICENSE, VERSION

# =============================================================================
# Module Exports
# =============================================================================

__all__: list[str] = [
    "StatusCommand",
    "VersionCommand",
    "CheckCommand",
    "GreetCommand",
    "create_parser",
    "main",
    "VERSION",
    "AUTHOR",
    "LICENSE",
]
