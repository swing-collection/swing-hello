# -*- coding: utf-8 -*-

"""
Status Command
==============

CLI command to check and display application status.

This command verifies that the Swing Hello application is properly
installed and displays key information about the environment.

Classes:
    StatusCommand: Check application status and configuration.

Output:
    - Application version
    - Django version
    - Persistence status (enabled/disabled)
    - Overall health status

Example:
    >>> cmd = StatusCommand()
    >>> cmd.run()
    Swing Hello Application Status
    ========================================
    Status:        OK
    Version:       0.3.0
    ...
    0
"""

# Import | Standard Library
import sys

# Import | Local
from .constants import VERSION


class StatusCommand:
    """
    CLI command to check and display application status.

    Performs health checks to verify the application is properly
    installed and functional. Displays version information, Django
    status, and persistence configuration.

    Methods:
        run: Execute the status check and display output.

    Example:
        >>> StatusCommand().run()
        Swing Hello Application Status
        ...
        0
    """

    def run(self) -> int:
        """
        Execute the status check and display results.

        Checks for Django availability, model imports, and persistence
        status. Outputs a formatted status report to stdout.

        Returns:
            0 on success, 1 if any imports fail or errors occur.

        Raises:
            Does not raise; catches exceptions and returns error code.
        """
        try:
            # Check if Django is available
            import django

            django_version = django.get_version()

            # Check if our models can be imported
            from swing.hello.models import PERSISTENCE_ENABLED

            print("Swing Hello Application Status")
            print("=" * 40)
            print("Status:        OK")
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


__all__: list[str] = ["StatusCommand"]
