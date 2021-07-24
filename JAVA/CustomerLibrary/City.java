import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;

public class City implements java.io.Serializable {
    private static final long serialVersionUID = 1L;
    private static final String statefile = "./city.data" ;
    private static String cityfile;
    int ID;
    String name;
    public City(int ID, String name) {
        this.ID = ID;
        this.name = name;
    }
    public int getID() {
        return ID;
    }
    public void setID(int ID) {
        this.ID = ID;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    @Override
    public String toString() {
        return "City [ID=" + ID + ", Name=" + name + "]";
    }

    // user interaction for State Object
    public static City add() {
        int     id;
        String  name;
        System.out.println("Please enter city id");
        id = Integer.parseInt(System.console().readLine());
        System.out.println("Please enter city name");
        name = System.console().readLine();
        return new City(id,name);
    }

    public static City update(City city) {
        int     id;
        String  name;
        System.out.println("State Information is:");
        System.out.println(city);  
        System.out.println("Please update city name");
        name = System.console().readLine();
        System.out.println("read name is " + name);
        city.name = name ;
        System.out.println("Updated name is " + city.name);
        return city ;
    }

    // callee will pass the citylist contianing list of cities to be saved / serialized
    public static void save(ArrayList<City> citylist) {
        System.out.print("Saving master state list in the file!!!");
        try {
            FileOutputStream fileOut =new FileOutputStream(cityfile);
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(citylist);
            out.close();
            fileOut.close();
            System.out.println("State data is saved!");
        } catch (IOException i) {
            i.printStackTrace();
        }
    }

    public static ArrayList<City> initializeFromFile() {
        try {
            File f = new File(cityfile) ;
            if (!f.exists()) {
                return new ArrayList<City>();
            }
            FileInputStream fileIn = new FileInputStream(cityfile);
            ObjectInputStream in = new ObjectInputStream(fileIn);
            ArrayList<City> citylist  = (ArrayList<City>) in.readObject();
            in.close();
            fileIn.close();
            return citylist ;
        } catch (IOException i) {
            i.printStackTrace();
            return null;
        } catch (ClassNotFoundException c) {
            System.out.println("City class not found");
            c.printStackTrace();
            return null;
        }
    }

    public static int findByID(ArrayList<City> list, int id) {
        int idx = -1;
        int size = list.size() ;
        for (int i = 0; i < size; i++) {
            if (list.get(i).getID() == id) {
                idx = i ;
            }
        }
        return idx ;
    }
}