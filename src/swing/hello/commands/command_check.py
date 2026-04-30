# -*- coding: utf-8 -*-

"""
Check Command
=============

CLI command to run Django system checks.
"""


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
            app_errors = [e for e in errors if "swing.hello" in str(e.obj) or not e.obj]

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
