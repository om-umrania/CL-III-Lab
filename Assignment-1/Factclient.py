# Factclient.py
# ----------------------------
# Client-side code for connecting to RPC server and invoking factorial computation

# Assignment 1
# Name: Om Umrania
# Roll Number: BEAD21163
# Subject: Computer Laboratory III (Computational Intelligence)

import datetime
import xmlrpc.client

# Establish a connection with the RPC server
with xmlrpc.client.ServerProxy("http://localhost:8000/RPC2") as proxy:
    try:
        # Take user input (or replace with any static integer)
        input_value = int(input("Enter a non-negative integer: "))
        result = proxy.calculate_factorial(input_value)
        print()
        print(f"[{datetime.datetime.now()}] Calculating factorial of {input_value}")
        print(f"✅ Factorial of {input_value} is: {result}")
    except Exception as e:
        print(f"❌ Error: {e}")