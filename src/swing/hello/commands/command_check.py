# -*- coding: utf-8 -*-

"""
Check Command
=============

CLI command to run Django system checks for this application.

This command runs Django's system check framework and reports any
warnings or errors specific to the swing.hello application.

Classes:
    CheckCommand: Run Django system checks.

Example:
    >>> cmd = CheckCommand()
    >>> cmd.run()
    Running Django system checks for swing.hello...
    ----------------------------------------
    No issues found!
    0

Note:
    Requires Django settings to be configured. If not configured,
    the command will skip checks gracefully.
"""


class CheckCommand:
    """
    CLI command to run Django system checks.

    Executes Django's system check framework and filters results
    to show only issues related to the swing.hello application.

    Methods:
        run: Execute system checks and display results.

    Example:
        >>> CheckCommand().run()
        No issues found!
        0
    """

    def run(self) -> int:
        """
        Execute Django system checks and display results.

        Runs all registered Django system checks and filters to show
        only issues relevant to the swing.hello application. Displays
        each issue with its severity level, ID, and hint if available.

        Returns:
            0 if no critical issues found, 1 if critical issues exist.

        Note:
            If Django settings are not configured, returns 0 without
            running checks.
        """
        try:
            import django
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
                level = str(error.level_tag).upper()  # type: ignore[attr-defined]
                print(f"[{level}] {error.id}: {error.msg}")
                if error.hint:
                    print(f"  Hint: {error.hint}")

            critical = [e for e in app_errors if e.is_serious()]
            if critical:
                return 1

            return 0

        except Exception as e:
            # Import | Standard Library
            import sys

            print(f"Error running checks: {e}", file=sys.stderr)
            return 1


__all__: list[str] = ["CheckCommand"]
