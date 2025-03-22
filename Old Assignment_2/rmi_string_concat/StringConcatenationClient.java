// File: StringConcatenationClient.java
// Client-side code to call remote method

package Assignment_2.rmi_string_concat;

import java.rmi.Naming;

public class StringConcatenationClient {
    public static void main(String[] args) {
        try {
            // Lookup the remote object via RMI registry
            StringConcatenator stub = (StringConcatenator) Naming.lookup("rmi://localhost:1099/concatService");

            // Sample strings to concatenate
            String str1 = "Hello, ";
            String str2 = "World!";

            // Call the remote method
            String result = stub.concatenate(str1, str2);

            // Display the result
            System.out.println("✅ Concatenated Result: " + result);
        } catch (Exception e) {
            System.err.println("Client Error: " + e.getMessage());
            e.printStackTrace();
        }
    }
}