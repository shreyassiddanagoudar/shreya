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

public class Category implements java.io.Serializable  {
    private static final long serialVersionUID = 1L;
    private static final String bookfile = "./category.data";

    String name;
    int id;
    public static long getSerialversionuid() {
        return serialVersionUID;
    }
    public static String getBookfile() {
        return bookfile;
    }
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
    public Category(String name, int id) {
        this.name = name;
        this.id = id;
    }
    public Category(int id2, String name2) {
    }
   
    @Override
    public String toString() {
        return "Category [id=" + id + ", name=" + name + "]";
    }


    public static void save(ArrayList<Category> catlist) {
        System.out.print("Saving master book list in the file!!!");
        try {
            FileOutputStream fileOut =new FileOutputStream(bookfile);
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(catlist);
            out.close();
            fileOut.close();
            System.out.println("Category data is saved!");
        } catch (IOException i) {
            i.printStackTrace();
        }
    }

    public static ArrayList<Category> initializeFromFile() {
        try {
            File f = new File(bookfile) ;
            if (!f.exists()) {
                return new ArrayList<Category>();
            }
            FileInputStream fileIn = new FileInputStream(bookfile);
            ObjectInputStream in = new ObjectInputStream(fileIn);
            ArrayList<Category> catlist  = (ArrayList<Category>) in.readObject();
            in.close();
            fileIn.close();
            return catlist ;
        } catch (IOException i) {
            i.printStackTrace();
            return null;
        } catch (ClassNotFoundException c) {
            System.out.println("Category class not found");
            c.printStackTrace();
            return null;
        }
    }


}