

public class Customer {
    int id;
    String name;
    int discount;
    public Customer(int id, String name, int discount) {
        this.id = id;
        this.name = name;
        this.discount = discount;
    }
    public int getID() {
        return id;
    }
    
    public String getName() {
        return name;
    }
   
    public int getDiscount() {
        return discount;
    }
    public void setDiscount(int discount) {
        this.discount = discount;
    }
    
    public String toString() {
        return "Customer [discount=" + discount + ", id=" + id + ", name=" + name + "]";
    }

}
