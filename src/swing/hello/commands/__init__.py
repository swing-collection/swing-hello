# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Swing Hello Commands Module
===========================

This module serves as the entry point for command-line utilities in the
`swing_hello` package. It centralizes available commands for easy imports.

Available Commands:
-------------------
- `StatusCommand` - Checks the status of the Swing Hello application.
- `VersionCommand` - Displays version information.
- `CheckCommand` - Runs Django system checks.
- `GreetCommand` - Generates a greeting from the command line.

Usage:
------
    from swing.hello.commands import StatusCommand, GreetCommand
    StatusCommand().run()
    GreetCommand(name="John", style="formal").run()
"""

# =============================================================================
# Imports
# =============================================================================


# Import | Local
# Import | Local Modules
from .command_status import (
    CheckCommand,
    create_parser,
    GreetCommand,
    main,
    StatusCommand,
    VERSION,
    VersionCommand,
)

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
]
