import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:9000")

while True:
    print("\n--- Hotel Booking Menu ---")
    print("1. Book a Room")
    print("2. Cancel Booking")
    print("3. View All Bookings")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        guest_name = input("Enter guest name: ")
        result = server.book_room(guest_name)
        print(result)
    elif choice == '2':
        guest_name = input("Enter guest name to cancel booking: ")
        result = server.cancel_booking(guest_name)
        print(result)
    elif choice == '3':
        bookings = server.view_bookings()
        if bookings:
            for guest, room in bookings.items():
                print(f"Guest: {guest}, Room: {room}")
        else:
            print("No current bookings.")
    elif choice == '4':
        print("Exiting the client...")
        break
    else:
        print("Invalid choice. Try again.")