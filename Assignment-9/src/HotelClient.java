import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class HotelClient {
    public static void main(String[] args) {
        try {
            Registry registry = LocateRegistry.getRegistry("localhost", 5050);
            HotelBooking stub = (HotelBooking) registry.lookup("HotelBookingService");
            Scanner sc = new Scanner(System.in);
            while (true) {
                System.out.print("1=Book, 2=Cancel, 0=Exit > ");
                int choice = sc.nextInt();
                if (choice == 0) break;
                System.out.print("Guest Name: ");
                String name = sc.next();
                System.out.print("Room No: ");
                int room = sc.nextInt();
                boolean result = (choice == 1)
                    ? stub.bookRoom(name, room)
                    : stub.cancelBooking(name, room);
                System.out.println(result ? "Success" : "Failed");
            }
            sc.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}