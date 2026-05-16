# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Greet Command
=============

CLI command to generate greetings from the command line.

This command generates and displays a greeting message for a given
name, with optional style customization.

Classes:
    GreetCommand: Generate a greeting message.

Styles:
    - formal: Professional greeting ("Good day, Name.")
    - casual: Friendly greeting ("Hello, Name!")
    - enthusiastic: Excited greeting ("Hey Name! So excited...")

Example:
    >>> cmd = GreetCommand(name='Alice', style='formal')
    >>> cmd.run()
    Good day, Alice. It is a pleasure to meet you.
    0
"""

# Import | Standard Library
import sys


class GreetCommand:
    """
    CLI command to generate a greeting message.

    Takes a name and optional style to generate an appropriate
    greeting message displayed to stdout.

    Attributes:
        name: The name to greet.
        style: Greeting style ('formal', 'casual', 'enthusiastic').

    Methods:
        run: Generate and display the greeting.

    Example:
        >>> GreetCommand('Bob', 'enthusiastic').run()
        Hey Bob! So excited to see you!
        0
    """

    def __init__(self, name: str, style: str = "casual") -> None:
        """
        Initialize the greet command.

        Args:
            name: The name to include in the greeting.
            style: The greeting style. One of 'formal', 'casual',
                or 'enthusiastic'. Defaults to 'casual'.
        """
        self.name = name
        self.style = style

    def run(self) -> int:
        """
        Generate and display a greeting message.

        Looks up the appropriate message template for the configured
        style and formats it with the name. Falls back to casual
        style if an unknown style is specified.

        Returns:
            0 on success, 1 on error.

        Example:
            >>> GreetCommand('Alice', 'formal').run()
            Good day, Alice. It is a pleasure to meet you.
            0
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


__all__: list[str] = ["GreetCommand"]
