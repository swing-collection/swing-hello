# -*- coding: utf-8 -*-

# =============================================================================
# Docstring
# =============================================================================

"""
Swing Hello CLI Entry Point
===========================

This script serves as the command-line entry point for the `swing.hello`
package.

Usage:
    python -m swing.hello
    python -m swing.hello status
    python -m swing.hello version
    python -m swing.hello check
    python -m swing.hello greet "John" --style formal
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
import sys

# Import | Local Modules
from swing.hello.commands.command_status import main as cli_main

# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    sys.exit(cli_main())


# =============================================================================
# Exports
# =============================================================================

__all__: list[str] = [
    "cli_main",
]
