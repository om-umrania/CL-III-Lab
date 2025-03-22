# Factserver.py
# ----------------------------
# Server-side code for distributed factorial computation using XML-RPC in Python

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Define the class with the factorial computation logic
class FactorialServer:
    def calculate_factorial(self, n):
        if n < 0:
            raise ValueError("Input must be a non-negative integer.")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Restrict server to respond only to '/RPC2' endpoint
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Initialize and configure the XML-RPC server
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    server.register_instance(FactorialServer())
    print("🟢 Factorial RPC Server is running on port 8000...")
    server.serve_forever()