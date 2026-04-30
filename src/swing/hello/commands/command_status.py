# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
CLI Commands for Swing Hello
============================

This module defines CLI commands for the Swing Hello application.

Commands:
    - status: Check if the application is running correctly.
    - version: Display version information.
    - check: Run Django system checks.
    - greet: Generate a greeting from the command line.

Usage:
    python -m swing.hello status
    python -m swing.hello version
    python -m swing.hello check
    python -m swing.hello greet "John"
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
import argparse
import sys
from typing import Sequence

# =============================================================================
# Version Info
# =============================================================================

VERSION = "0.3.0"
AUTHOR = "Lars van Vianen"
LICENSE = "BSD 3-Clause"


# =============================================================================
# Command Classes
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
            # Check if Django is available
            import django

            django_version = django.get_version()

            # Check if our models can be imported
            from swing.hello.models import PERSISTENCE_ENABLED

            print("Swing Hello Application Status")
            print("=" * 40)
            print(f"Status:        OK")
            print(f"Version:       {VERSION}")
            print(f"Django:        {django_version}")
            print(
                f"Persistence:   {'Enabled' if PERSISTENCE_ENABLED else 'Disabled'}"
            )
            print("=" * 40)
            print("Application is running successfully!")
            return 0

        except ImportError as e:
            print(f"Import Error: {e}", file=sys.stderr)
            return 1
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1


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


class CheckCommand:
    """
    CLI Command to Run Django System Checks
    ========================================

    Runs Django's system check framework for this app.
    """

    def run(self) -> int:
        """
        Run Django system checks.

        Returns:
            int: Exit code (0 if no issues, 1 if issues found).
        """
        try:
            import django
            from django.core import checks
            from django.core.checks.registry import registry

            # Setup Django if not already configured
            if not django.conf.settings.configured:
                print("Django settings not configured. Skipping checks.")
                return 0

            print("Running Django system checks for swing.hello...")
            print("-" * 40)

            # Get all checks for this app
            errors = registry.run_checks(
                app_configs=None,
                tags=None,
                include_deployment_checks=False,
            )

            # Filter to our app
            app_errors = [
                e for e in errors if "swing.hello" in str(e.obj) or not e.obj
            ]

            if not app_errors:
                print("No issues found!")
                return 0

            for error in app_errors:
                level = error.level_tag.upper()
                print(f"[{level}] {error.id}: {error.msg}")
                if error.hint:
                    print(f"  Hint: {error.hint}")

            critical = [e for e in app_errors if e.is_serious()]
            if critical:
                return 1

            return 0

        except Exception as e:
            print(f"Error running checks: {e}", file=sys.stderr)
            return 1


class GreetCommand:
    """
    CLI Command to Generate a Greeting
    ===================================

    Generate a greeting from the command line.
    """

    def __init__(self, name: str, style: str = "casual") -> None:
        """
        Initialize the greet command.

        Args:
            name: The name to greet.
            style: The greeting style (formal, casual, enthusiastic).
        """
        self.name = name
        self.style = style

    def run(self) -> int:
        """
        Generate and display a greeting.

        Returns:
            int: Exit code (0 for success, 1 for error).
        """
        try:
            messages = {
                "formal": f"Good day, {self.name}. It is a pleasure to meet you.",
                "casual": f"Hello, {self.name}!",
                "enthusiastic": f"Hey {self.name}! So excited to see you!",
            }

            message = messages.get(self.style, messages["casual"])
            print(message)
            return 0

        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1


# =============================================================================
# CLI Parser
# =============================================================================


def create_parser() -> argparse.ArgumentParser:
    """
    Create the argument parser for the CLI.

    Returns:
        argparse.ArgumentParser: The configured parser.
    """
    parser = argparse.ArgumentParser(
        prog="swing-hello",
        description="Swing Hello CLI - A Django greeting application",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        title="commands",
        description="Available commands",
    )

    # Status command
    subparsers.add_parser(
        "status",
        help="Check application status",
    )

    # Version command
    subparsers.add_parser(
        "version",
        help="Display version information",
    )

    # Check command
    subparsers.add_parser(
        "check",
        help="Run Django system checks",
    )

    # Greet command
    greet_parser = subparsers.add_parser(
        "greet",
        help="Generate a greeting",
    )
    greet_parser.add_argument(
        "name",
        type=str,
        help="The name to greet",
    )
    greet_parser.add_argument(
        "-s",
        "--style",
        type=str,
        choices=["formal", "casual", "enthusiastic"],
        default="casual",
        help="Greeting style (default: casual)",
    )

    return parser


def main(args: Sequence[str] | None = None) -> int:
    """
    Main entry point for the CLI.

    Args:
        args: Command line arguments (defaults to sys.argv).

    Returns:
        int: Exit code.
    """
    parser = create_parser()
    parsed = parser.parse_args(args)

    if parsed.command == "status" or parsed.command is None:
        return StatusCommand().run()
    elif parsed.command == "version":
        return VersionCommand().run()
    elif parsed.command == "check":
        return CheckCommand().run()
    elif parsed.command == "greet":
        return GreetCommand(
            name=parsed.name,
            style=parsed.style,
        ).run()
    else:
        parser.print_help()
        return 0


# =============================================================================
# Exports
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
