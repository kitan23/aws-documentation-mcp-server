#!/usr/bin/env python
"""Main entry point for AWS Documentation MCP Server.

This file serves as the entry point for Lambda deployment.
It imports and runs the main function from the appropriate server module.
"""

import os
import sys

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import and run the main function from the server module
from awslabs.aws_documentation_mcp_server.server import main

if __name__ == '__main__':
    main()