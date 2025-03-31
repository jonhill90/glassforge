#!/bin/bash

# Default behavior: drop into an interactive shell
# You could add options here to auto-run Glassforge routines in the future

echo "Starting Glassforge container..."
exec "$@"
