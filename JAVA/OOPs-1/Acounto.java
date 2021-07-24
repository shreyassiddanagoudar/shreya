public class Acounto {
    String ID;
    String Name;
    int Balance=0;
    public String getID() {
        return ID;
    }
    public String getName() {
        return Name;
    }
   public int getBalance() {
        return Balance;
    }
   
    public int getAmount() {
        return Amount;
    }
    public void setAmount(int amount) {
        Amount = amount;
    }
    public Acounto credit() {
        if(this.amount<=Balance);
       amount= amount-Balance;
    } else {
        return Balance;
    }
    public Acounto debitt(amount:int) {
        if(this.amount>=Balance);
       amount= amount+Balance;
    } else {
        return Balance;
    }
    public String toString() {
        return "Acounto [Balance=" + Balance + ", ID=" + ID + ", Name=" + Name + "]";
    }
    public Acounto(String iD, String name, int balance) {
        this.ID = iD;
        this.Name = name;
        this.Balance = balance;
    }
   
}
