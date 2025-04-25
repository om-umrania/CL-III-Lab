import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;
import java.util.HashMap;
import java.util.Map;

public class HotelServer implements HotelBooking {
    private final Map<Integer, String> bookings = new HashMap<>();

    public HotelServer() { }

    @Override
    public synchronized boolean bookRoom(String guestName, int roomNo) {
        if (bookings.containsKey(roomNo)) return false;
        bookings.put(roomNo, guestName);
        System.out.println("Booked room " + roomNo + " for " + guestName);
        return true;
    }

    @Override
    public synchronized boolean cancelBooking(String guestName, int roomNo) {
        if (guestName.equals(bookings.get(roomNo))) {
            bookings.remove(roomNo);
            System.out.println("Cancelled room " + roomNo + " for " + guestName);
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        try {
            HotelServer obj = new HotelServer();
            HotelBooking stub = (HotelBooking) UnicastRemoteObject.exportObject(obj, 0);
            Registry registry = LocateRegistry.createRegistry(5050);
            registry.rebind("HotelBookingService", stub);
            System.out.println("HotelServer ready on port 5050.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}