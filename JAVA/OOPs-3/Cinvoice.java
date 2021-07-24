public class Cinvoice {
    int id;
    String name;
    int discount;
    public Cinvoice(int id, String name, int discount) {
        this.id = id;
        this.name = name;
        this.discount = discount;
    }
    public int getId() {
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
        return "Cinvoice [discount=" + discount + ", id=" + id + ", name=" + name + "]";
    }
}
