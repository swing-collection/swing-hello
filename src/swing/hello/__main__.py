# -*- coding: utf-8 -*-

# =============================================================================
# Docstring
# =============================================================================

"""
Swing Hello CLI Entry Point
===========================

This script serves as the command-line entry point for the `swing.hello`
package. It executes the `StatusCommand` when run as a script.

Usage:
    python -m swing_hello
"""


# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
import sys
from typing import List

# Import | Local Modules
from swing.hello.commands import StatusCommand

# Import | Libraries


# =============================================================================
# Functions
# =============================================================================


def main() -> int:
    """
    Executes the StatusCommand.

    Returns:
        int: The exit code of the command execution.
    """
    return StatusCommand().run()


# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    sys.exit(status=main())


# =============================================================================
# Exports
# =============================================================================

__all__: List[str] = [
    "main",
]
