# client.py
# ----------------------------
# Client-side code to access string concatenation via Pyro4 remote server

import Pyro4

def main():
    # Read the server URI stored by the server
    with open("server_uri.txt", "r") as f:
        uri = f.read().strip()

    # Create a proxy object for the remote server
    server = Pyro4.Proxy(uri)

    # Take two string inputs from the user
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")

    # Call remote method
    result = server.concatenate_strings(str1, str2)

    # Show result
    print("✅ Concatenated Result:", result)

if __name__ == "__main__":
    main()