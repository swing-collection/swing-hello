# -*- coding: utf-8 -*-

"""
Version Command
===============

CLI command to display version information.
"""

# Import | Local
from .constants import AUTHOR, LICENSE, VERSION


class VersionCommand:
    """
    CLI Command to Display Version Information
    ==========================================

    Displays the version of the Swing Hello application.
    """

    def run(self) -> int:
        """
        Display version information.

        Returns:
            int: Exit code (always 0).
        """
        print(f"swing-hello {VERSION}")
        print(f"Author: {AUTHOR}")
        print(f"License: {LICENSE}")
        return 0


__all__: list[str] = ["VersionCommand"]
