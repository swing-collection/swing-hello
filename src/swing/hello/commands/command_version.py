# -*- coding: utf-8 -*-

"""
Version Command
===============

CLI command to display version and package information.

This command outputs the application version, author, and license
information to stdout.

Classes:
    VersionCommand: Display version information.

Example:
    >>> cmd = VersionCommand()
    >>> cmd.run()
    swing-hello 0.3.0
    Author: Lars van Vianen
    License: BSD 3-Clause
    0
"""

# Import | Local
from .constants import AUTHOR, LICENSE, VERSION


class VersionCommand:
    """
    CLI command to display version and package information.

    Outputs the application version, author name, and license
    to stdout in a human-readable format.

    Methods:
        run: Display version information.

    Example:
        >>> VersionCommand().run()
        swing-hello 0.3.0
        ...
        0
    """

    def run(self) -> int:
        """
        Display version, author, and license information.

        Returns:
            Always returns 0 (success).
        """
        print(f"swing-hello {VERSION}")
        print(f"Author: {AUTHOR}")
        print(f"License: {LICENSE}")
        return 0


__all__: list[str] = ["VersionCommand"]
