public class Customera1 {
    int id;
    String name;
    char gender;
    
   
    public int getId() {
        return id;
    }
    
    public String getName() {
        return name;
    }
   
    public char getGender() {
        return gender;
    }
    public Customera1(int id, String name, char gender) {
        this.id = id;
        this.name = name;
        this.gender = gender;
    }
    public String toString() {
        return "Customera1 [gender=" + gender + ", id=" + id + ", name=" + name + "]";
    }
}
