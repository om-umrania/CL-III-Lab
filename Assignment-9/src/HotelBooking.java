import java.rmi.Remote;
import java.rmi.RemoteException;

public interface HotelBooking extends Remote {
    boolean bookRoom(String guestName, int roomNo) throws RemoteException;
    boolean cancelBooking(String guestName, int roomNo) throws RemoteException;
}