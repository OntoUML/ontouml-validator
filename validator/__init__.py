import sys

import loguru

# Create a logger object
logger = loguru.logger

# Add a handler to the logger for the screen
logger.add(sys.stderr)

# Set the global log level:
logger.level("INFO")
