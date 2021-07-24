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

public class Author implements java.io.Serializable  {
    private static final long serialVersionUID = 1L;
    private static final String bookfile = "./Author.data";
    String name;
    int id;
    String email;
    String adress;
    
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
    public String getAdress() {
        return adress;
    }
    public void setAdress(String adress) {
        this.adress = adress;
    }
    public Author(String name, int id, String email, String adress) {
        this.name = name;
        this.id = id;
        this.email = email;
        this.adress = adress;
    }
    @Override
    public String toString() {
        return "Author [adress=" + adress + ", email=" + email + ", id=" + id + ", name=" + name + "]";
    }


    public static void save(ArrayList<Author> authlist) {
        System.out.print("Saving master book list in the file!!!");
        try {
            FileOutputStream fileOut =new FileOutputStream(bookfile);
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(authlist);
            out.close();
            fileOut.close();
            System.out.println("Author data is saved!");
        } catch (IOException i) {
            i.printStackTrace();
        }
    }

    public static ArrayList<Author> initializeFromFile() {
        try {
            File f = new File(bookfile) ;
            if (!f.exists()) {
                return new ArrayList<Author>();
            }
            FileInputStream fileIn = new FileInputStream(bookfile);
            ObjectInputStream in = new ObjectInputStream(fileIn);
            ArrayList<Author> authlist  = (ArrayList<Author>) in.readObject();
            in.close();
            fileIn.close();
            return authlist ;
        } catch (IOException i) {
            i.printStackTrace();
            return null;
        } catch (ClassNotFoundException c) {
            System.out.println("Authort class not found");
            c.printStackTrace();
            return null;
        }
    }
}