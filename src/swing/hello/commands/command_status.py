# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Status Command for Swing Hello
==============================

This module defines the `StatusCommand` class, which serves as a command-line
utility to check the status of the `swing_hello` application.

Usage:
    from swing.hello.commands import StatusCommand
    StatusCommand().run()
"""

# =============================================================================
# Imports
# =============================================================================

import sys
from typing import List

# =============================================================================
# StatusCommand Class
# =============================================================================


class StatusCommand:
    """
    CLI Command to Check Application Status
    =======================================

    This command provides a simple check to confirm that the `swing.hello`
    application is correctly installed and functional.

    """

    def run(self) -> int:
        """
        Executes the status check.

        Returns:
            int: Exit code (0 for success, non-zero for failure).
        """
        try:
            print("Swing Hello application is running successfully!")
            return 0
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1


# =============================================================================
# Exports
# =============================================================================

__all__: List[str] = [
    "StatusCommand",
]
