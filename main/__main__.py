#!/usr/bin/env python
"""Main module entry point for AWS Documentation MCP Server.

This allows the server to be run with `python -m main`.
"""

import os
import sys
import argparse

# Add parent directory to path to find awslabs module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Parse command line arguments (to handle --port 8080 from the Dockerfile)
# We parse but ignore them since the port is already configured in server code
parser = argparse.ArgumentParser(description='AWS Documentation MCP Server')
parser.add_argument('--port', type=int, default=8080, help='Port to run on (ignored, uses 8080 from server config)')
parser.add_argument('--host', type=str, default='0.0.0.0', help='Host to bind to (ignored)')
args, unknown = parser.parse_known_args()  # Use parse_known_args to ignore any extra arguments

# Import and run the main function from the server module
from awslabs.aws_documentation_mcp_server.server import main

if __name__ == '__main__':
    # The port is already configured to 8080 in the server code
    main()
else:
    # Also support running as a module
    main()