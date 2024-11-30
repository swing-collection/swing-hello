# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Django's command-line utility for administrative tasks.
"""

import os
import sys
from pathlib import Path


# Add `src` directory to Python path
DEMO_DIR = Path(__file__).resolve().parent
BASE_DIR = DEMO_DIR.resolve().parent
sys.path.append(str(BASE_DIR / "src"))

def main():
    """
    Run administrative tasks.
    """

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')

    try:
        from django.core.management import execute_from_command_line

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
