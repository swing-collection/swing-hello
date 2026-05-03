# -*- coding: utf-8 -*-

"""
CLI Constants
=============

Version and metadata constants for the Swing Hello CLI.

These constants are used throughout the CLI for version display,
status output, and package metadata.

Constants:
    VERSION: Semantic version string (e.g., "0.3.0").
    AUTHOR: Package author name.
    LICENSE: SPDX license identifier.

Example:
    >>> from swing.hello.commands.constants import VERSION
    >>> print(f'swing-hello v{VERSION}')
    swing-hello v0.3.0
"""

VERSION: str = "0.3.0"
"""Current version of the Swing Hello application."""

AUTHOR: str = "Lars van Vianen"
"""Package author and maintainer."""

LICENSE: str = "BSD 3-Clause"
"""SPDX license identifier for the package."""


__all__: list[str] = ["VERSION", "AUTHOR", "LICENSE"]
