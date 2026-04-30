# -*- coding: utf-8 -*-

"""
Greet Command
=============

CLI command to generate a greeting from the command line.
"""

# Import | Standard Library
import sys


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


__all__: list[str] = ["GreetCommand"]
