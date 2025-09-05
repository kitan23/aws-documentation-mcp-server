#!/usr/bin/env python
"""Main entry point for AWS Documentation MCP Server.

This file serves as the entry point for Lambda deployment.
It imports and runs the main function from the appropriate server module.
"""

import os
import sys

# Add the current directory to the Python path to ensure modules can be found
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    # Parse command line arguments (to handle --port 8080 from the Dockerfile)
    # We parse but ignore them since the port is already configured in server code
    import argparse
    parser = argparse.ArgumentParser(description='AWS Documentation MCP Server')
    parser.add_argument('--port', type=int, default=8080, help='Port to run on (ignored, uses 8080 from server config)')
    parser.add_argument('--host', type=str, default='0.0.0.0', help='Host to bind to (ignored)')
    args, unknown = parser.parse_known_args()  # Use parse_known_args to ignore any extra arguments
    
    # Import and run the main function from the server module
    from awslabs.aws_documentation_mcp_server.server import main
    
    # The port is already configured to 8080 in the server code
    main()