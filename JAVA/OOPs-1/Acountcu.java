public class Acountcu {
    int id;
    Customera1 customera1;
    double balance = 0.0;
    public Acountcu(int id, Customera1 customera1, double balance) {
        this.id = id;
        this.customera1 = customera1;
        this.balance = balance;
    }
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public Customera1 getCustomera1() {
        return customera1;
    }
    public void setCustomera1(Customera1 customera1) {
        this.customera1 = customera1;
    }
    public double getBalance() {
        return balance;
    }
    public void setBalance(double balance) {
        this.balance = balance;
    }
    @Override
    public String toString() {
        return "Acountcu [balance=" + balance + ", customera1=" + customera1 + ", id=" + id + "]";
    }
}
  