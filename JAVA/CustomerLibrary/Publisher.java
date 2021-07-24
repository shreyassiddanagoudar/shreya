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

public class Publisher implements java.io.Serializable  {
    private static final long serialVersionUID = 1L;
    private static final String bookfile = "./publisher.data";
    String name;
    int id;
    String email;
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public String getEmail() {
        return email;
    }
    public void setEmail(String email) {
        this.email = email;
    }
    public Publisher(String name, int id, String email) {
        this.name = name;
        this.id = id;
        this.email = email;
    }
    @Override
    public String toString() {
        return "Publisher [email=" + email + ", id=" + id + ", name=" + name + "]";
    }


    public static void save(ArrayList<Publisher> publist) {
        System.out.print("Saving master book list in the file!!!");
        try {
            FileOutputStream fileOut =new FileOutputStream(bookfile);
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(publist);
            out.close();
            fileOut.close();
            System.out.println("Publisher data is saved!");
        } catch (IOException i) {
            i.printStackTrace();
        }
    }

    public static ArrayList<Publisher> initializeFromFile() {
        try {
            File f = new File(bookfile) ;
            if (!f.exists()) {
                return new ArrayList<Publisher>();
            }
            FileInputStream fileIn = new FileInputStream(bookfile);
            ObjectInputStream in = new ObjectInputStream(fileIn);
            ArrayList<Publisher> publist  = (ArrayList<Publisher>) in.readObject();
            in.close();
            fileIn.close();
            return publist ;
        } catch (IOException i) {
            i.printStackTrace();
            return null;
        } catch (ClassNotFoundException c) {
            System.out.println("Publisher class not found");
            c.printStackTrace();
            return null;
        }
    }
}
