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

Usage:
------
    from swing_hello.commands import StatusCommand
    StatusCommand().run()

"""


# =============================================================================
# Imports
# =============================================================================

from typing import List

# Import | Local Modules
from .command_status import StatusCommand

# =============================================================================
# Module Exports
# =============================================================================

__all__: List[str] = [
    "StatusCommand",
]
