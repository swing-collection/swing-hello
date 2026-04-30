# -*- coding: utf-8 -*-

"""
CLI Parser
==========

Command-line argument parser for the Swing Hello application.
"""

# Import | Standard Library
import argparse


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


__all__: list[str] = ["create_parser"]
