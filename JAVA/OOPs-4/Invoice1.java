

public class Invoice1 {
    int id;
    Customer customer;
    double amount;
    
    public int getID() {
        return id;
    }
   
    public Customer getCustomer() {
        return customer;
    }
    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public double getAmount() {
        return amount;
    }
    public void setAmount(double amount) {
        this.amount = amount;
    }
    public int getCustomerID(){
        return customer.getID();
    }
    public String getCustomerName(){
        return customer.getName();
    }
    public double getCustomerDiscount(){
        return customer.getDiscount();
    }
    public double getAmountAfterDiscount(){
        return amount-(amount*customer.getDiscount()/100);
    }
    
    public Invoice1(int id, Customer customer, double amount) { // property of an object(instance(wrt DT))
        this.id = id;                                           // accessing those properties by (this.variable = arguments/values)
        this.customer = customer;                                                               //  (key        =  value)
        this.amount = amount;
    }
    public String toString() {                                // Constructor(have same name as declared class)-accepts the arguments(values) that new object uses to set member variable
        return "Invoice1 [amount=" + amount + ", customer=" + customer + ", id=" + id + "]";
    }
}
