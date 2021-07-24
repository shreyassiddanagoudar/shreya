public class Custinvoice {
    int id;
    Coustmer coustmer;
    double amount;
    public Custinvoice(int id, Coustmer coustmer, double amount) {
        this.id = id;
        this.coustmer = coustmer;
        this.amount = amount;
    }
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public Coustmer getCoustmer() {
        return coustmer;
    }
    public void setCoustmer(Coustmer coustmer) {
        this.coustmer = coustmer;
    }
    public double getAmount() {
        return amount;
    }
    public void setAmount(double amount) {
        this.amount = amount;
    }
    @Override
    public String toString() {
        return "Custinvoice [amount=" + amount + ", coustmer=" + coustmer + ", id=" + id + "]";
    }
}