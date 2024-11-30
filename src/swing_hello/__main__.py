# -*- coding: utf-8 -*-


# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
import sys

# Import | Libraries

# Import | Local Modules
from swing_hello.commands import StatusCommand


# =============================================================================
# Functions
# =============================================================================

def main():
    return StatusCommand().run()


# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    sys.exit(main())


# =============================================================================
# Exports
# =============================================================================

__all__ = ["main"]