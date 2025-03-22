from xmlrpc.server import SimpleXMLRPCServer

class HotelBookingServer:
    def __init__(self):
        self.bookings = {}  # guest_name -> room_number
        self.room_counter = 1  # simple incremental room assignment

    def book_room(self, guest_name):
        if guest_name in self.bookings:
            return f"Guest '{guest_name}' already has room {self.bookings[guest_name]} booked."
        room_number = self.room_counter
        self.bookings[guest_name] = room_number
        self.room_counter += 1
        return f"Room {room_number} successfully booked for '{guest_name}'."

    def cancel_booking(self, guest_name):
        if guest_name in self.bookings:
            room_number = self.bookings.pop(guest_name)
            return f"Booking for guest '{guest_name}' (Room {room_number}) cancelled."
        else:
            return f"No booking found for guest '{guest_name}'."

    def view_bookings(self):
        return self.bookings

# Setup Server
server = SimpleXMLRPCServer(("localhost", 9000))
print("Hotel Booking Server is running on port 9000...")

hotel_server = HotelBookingServer()
server.register_instance(hotel_server)

# Keep server running
server.serve_forever()