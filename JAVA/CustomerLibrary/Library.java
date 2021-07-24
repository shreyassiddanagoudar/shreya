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

public class Library implements java.io.Serializable  {
    private static final long serialVersionUID = 1L;
    private static final String bookfile = "./library.data";

    String name;
    int id;
    String adress;
    String librarian;
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
    public String getAdress() {
        return adress;
    }
    public void setAdress(String adress) {
        this.adress = adress;
    }
    public String getLibrarian() {
        return librarian;
    }
    public void setLibrarian(String librarian) {
        this.librarian = librarian;
    }
    public Library(String name, int id, String adress, String librarian) {
        this.name = name;
        this.id = id;
        this.adress = adress;
        this.librarian = librarian;
    }
    @Override
    public String toString() {
        return "Library [adress=" + adress + ", id=" + id + ", librarian=" + librarian + ", name=" + name + "]";
    }

    public static void save(ArrayList<Library> liblist) {
        System.out.print("Saving master book list in the file!!!");
        try {
            FileOutputStream fileOut =new FileOutputStream(bookfile);
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(liblist);
            out.close();
            fileOut.close();
            System.out.println("Book data is saved!");
        } catch (IOException i) {
            i.printStackTrace();
        }
    }

    public static ArrayList<Library> initializeFromFile() {
        try {
            File f = new File(bookfile) ;
            if (!f.exists()) {
                return new ArrayList<Library>();
            }
            FileInputStream fileIn = new FileInputStream(bookfile);
            ObjectInputStream in = new ObjectInputStream(fileIn);
            ArrayList<Library> liblist  = (ArrayList<Library>) in.readObject();
            in.close();
            fileIn.close();
            return liblist ;
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
