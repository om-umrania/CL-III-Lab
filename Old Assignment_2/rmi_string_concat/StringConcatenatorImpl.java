// File: StringConcatenatorImpl.java
// Implementation of Remote Interface

package Assignment_2.rmi_string_concat;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class StringConcatenatorImpl extends UnicastRemoteObject implements StringConcatenator {

    // Constructor must throw RemoteException
    public StringConcatenatorImpl() throws RemoteException {
        super();
    }

    // Implement the remote method
    @Override
    public String concatenate(String str1, String str2) throws RemoteException {
        return str1 + str2;
    }
}