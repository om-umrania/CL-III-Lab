// File: StringConcatenator.java
// Remote Interface for String Concatenation using Java RMI

package Assignment_2.rmi_string_concat;

import java.rmi.Remote;
import java.rmi.RemoteException;

/**
 * Remote Interface for String Concatenation using Java RMI
 */
public interface StringConcatenator extends Remote {
    
    /**
     * Remote method to concatenate two strings.
     *
     * @param str1 First string
     * @param str2 Second string
     * @return Concatenated result of str1 and str2
     * @throws RemoteException if remote invocation fails
     */
    String concatenate(String str1, String str2) throws RemoteException;
}