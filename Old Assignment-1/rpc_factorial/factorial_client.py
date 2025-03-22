# factorial_client.py
# Client Program for Remote Factorial Calculation using XML-RPC
# Author: Om Umrania | CL-III Assignment 1

import xmlrpc.client

# Create a proxy object to communicate with the RPC server
proxy = xmlrpc.client.ServerProxy("http://localhost:9000/")

# Get integer input from the user
n = int(input("Enter a non-negative integer: "))

# Invoke the remote factorial function via proxy
result = proxy.calculate_factorial(n)

# Display the result returned by the server
print(f"Factorial of {n} is: {result}")