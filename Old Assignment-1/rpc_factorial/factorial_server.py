# factorial_server.py
# Server Program for Remote Factorial Calculation using XML-RPC
# Author: Om Umrania | CL-III Assignment 1

from xmlrpc.server import SimpleXMLRPCServer

# Define the factorial calculation logic
def calculate_factorial(n):
    """
    Calculates factorial of a non-negative integer n.
    Returns factorial if n >= 0, else returns error message.
    """
    if n < 0:
        return "Factorial not defined for negative numbers."
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

# Create an instance of XML-RPC server bound to localhost and port 9000
server = SimpleXMLRPCServer(("localhost", 9000))
print("🟢 XML-RPC Server is running on port 9000...")

# Register the factorial function as a callable RPC method
server.register_function(calculate_factorial, "calculate_factorial")

# Keep the server running and listening for client requests
server.serve_forever()