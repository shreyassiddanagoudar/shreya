import java.lang.Thread;
public class Tthreadshared  {
    public static void main(String[] args) {
        Accounts accountObject = new Accounts (); 
        accountObject.doOperation('D',1000);
        Thread t1 = new Thread(new TDeposit(accountObject));
        Thread t2 = new Thread(new TWithdraw(accountObject));
        Thread t3 = new Thread(new TEnquire(accountObject));
        t1.start();
        t2.start();
        t3.start();    


        Accounts1 ac1 = new Accounts1(); 
        ac1.doOperation('D',1000);
        Thread t11 = new Thread(new TDeposit1(ac1));
        Thread t21 = new Thread(new TWithdraw1(ac1));
        Thread t31 = new Thread(new TEnquire1(ac1));
        System.out.println("Deposit thread started");
        t11.start();
        // t11.join();
        System.out.println("Withdraw thread started");
        t21.start();
        System.out.println("Enquire thread started");
        t31.start();
    } 
}