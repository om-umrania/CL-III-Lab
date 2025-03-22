// File: StringConcatenationServer.java
// Server-side code to bind the remote object

package Assignment_2.rmi_string_concat;

import java.rmi.Naming;
import java.rmi.RemoteException;

public class StringConcatenationServer {
    public static void main(String[] args) {
        try {
            // Create remote object instance
            StringConcatenator stub = new StringConcatenatorImpl();

            // Bind the remote object in the registry
            Naming.rebind("rmi://localhost:1099/concatService", stub);

            System.out.println("🟢 String Concatenation RMI Server is running...");
        } catch (RemoteException e) {
            System.err.println("RemoteException: " + e.getMessage());
            e.printStackTrace();
        } catch (Exception e) {
            System.err.println("Server Error: " + e.getMessage());
            e.printStackTrace();
        }
    }
}