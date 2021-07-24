public class Person {
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
    public Person(String name, int id, String email) {
        this.name = name;
        this.id = id;
        this.email = email;
    }
    @Override
    public String toString() {
        return "Person [email=" + email + ", id=" + id + ", name=" + name + "]";
    }
}
