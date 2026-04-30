# -*- coding: utf-8 -*-

"""
Status Command
==============

CLI command to check application status.
"""

# Import | Standard Library
import sys

# Import | Local
from .constants import VERSION


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


__all__: list[str] = ["StatusCommand"]
