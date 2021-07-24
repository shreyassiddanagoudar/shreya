import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class Customer implements java.io.Serializable  {
    private static final long serialVersionUID = 1L;
    private static final String bookfile = "./cust.data";
    private static ArrayList<Customer> custlist;

    int accountid;
    int joindate;
    int lasttransdata;
    int numofbooks;
    public int getAccountid() {
        return accountid;
    }
    public void setAccountid(int accountid) {
        this.accountid = accountid;
    }
    public int getJoindate() {
        return joindate;
    }
    public void setJoindate(int joindate) {
        this.joindate = joindate;
    }
    public int getLasttransdata() {
        return lasttransdata;
    }
    public void setLasttransdata(int lasttransdata) {
        this.lasttransdata = lasttransdata;
    }
    public int getNumofbooks() {
        return numofbooks;
    }
    public void setNumofbooks(int numofbooks) {
        this.numofbooks = numofbooks;
    }
    public Customer(int accountid, int joindate, int lasttransdata, int numofbooks) {
        this.accountid = accountid;
        this.joindate = joindate;
        this.lasttransdata = lasttransdata;
        this.numofbooks = numofbooks;
    }
    @Override
    public String toString() {
        return "Customer [accountid=" + accountid + ", joindate=" + joindate + ", lasttransdata=" + lasttransdata
                + ", numofbooks=" + numofbooks + "]";
    }

    public static void save(ArrayList<Customer> custlist) {
        System.out.print("Saving master book list in the file!!!");
        try {
            FileOutputStream fileOut =new FileOutputStream(bookfile);
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(custlist);
            out.close();
            fileOut.close();
            System.out.println("Book data is saved!");
        } catch (IOException i) {
            i.printStackTrace();
        }
    }

    public static ArrayList<Customer> initializeFromFile() {
        try {
            File f = new File(bookfile) ;
            if (!f.exists()) {
                return new ArrayList<Customer>();
            }
            FileInputStream fileIn = new FileInputStream(bookfile);
            ObjectInputStream in = new ObjectInputStream(fileIn);
            ArrayList<Customer> custlist  = (ArrayList<Customer>) in.readObject();
            in.close();
            fileIn.close();
            return custlist ;
        } catch (IOException i) {
            i.printStackTrace();
            return null;
        } catch (ClassNotFoundException c) {
            System.out.println("Library class not found");
            c.printStackTrace();
            return null;
        }
    }
}
