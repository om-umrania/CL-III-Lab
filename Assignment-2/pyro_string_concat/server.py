# server.py
# ----------------------------
# Server-side code for distributed string concatenation using Pyro4 (Python RMI)

import Pyro4

# Assignment 2
# Name: Om Umrania
# Roll Number: BEAD21163
# Subject: Computer Laboratory III (Computational Intelligence)


# Decorator to expose this class to Pyro4 clients
@Pyro4.expose
class StringConcatenationServer:
    def concatenate_strings(self, str1, str2):
        """Concatenates two strings and returns the result."""
        return str1 + str2

def main():
    # Start the Pyro daemon
    daemon = Pyro4.Daemon()

    # Locate the Pyro Name Server running in background
    ns = Pyro4.locateNS()

    # Create an instance of the server
    server = StringConcatenationServer()

    # Register server with Pyro Daemon
    uri = daemon.register(server)

    # Register the object name in the Name Server
    ns.register("string.concatenation", uri)

    print("🟢 StringConcatenationServer is running...")
    print("Server URI:", uri)

    # Save URI in a file (optional but useful for client connection)
    with open("server_uri.txt", "w") as f:
        f.write(str(uri))

    # Start the event loop to wait for client requests
    daemon.requestLoop()

if __name__ == "__main__":
    main()