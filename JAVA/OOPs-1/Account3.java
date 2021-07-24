package OOPs;
//class method and variable
public class Account2 {
    static int Numofaccounts=0;
    int number;//class state variable
    float balance;//class state variable
    int numTrans = 0;
    char[] transtype;
    float [] transamount;
   //instance variables can be accessed only within method or you need to have instance of class
    public static void main(String args[]) {//creating an account
        Account account = new Account(); //Account is a class and account is an instance of class Account--object--why new?
        Account.Numofaccounts +=1;//class method and variable
        account.initialize(123);
        account.deposit(100);
        account.deposit(200);
        account.withdraw(50);  
        account.transaction(); 
        
    }
    static void printNumofaccounts() {//class method and variable
    Account.printNumofaccounts();//classmethod and variable
}
    void initialize(int num) {
        transtype = new char[100];
        transamount = new float[100];
        numTrans = 0;
        number = num;
    }
    void withdraw(float amount) {
        if (balance>amount) {
            System.out.println("withdrawing ammount " + amount);
            transamount[numTrans] = amount;
            transtype[numTrans] = 'W';
            numTrans++;
            balance = balance-amount;
        } else {
            System.out.println("Balance low ! can not withdraw amount " + amount);
            }
    }
        void deposit(float amount) {
            System.out.println("depositing amount " + amount);
            transamount[numTrans] = amount;
            transtype[numTrans] = 'D';
            numTrans++;
            balance = balance + amount;

        }
        void transaction() {
        System.out.println("=====================================================================================");
        System.out.println("                       Account Transaction on number :" +number);
        System.out.println("=====================================================================================");
        System.out.println("\tSl No. \t\t Description \t Deposit\t withdraw \t Balance");
        float balance = 0.0f;
        for(int i=0; i<numTrans; i++) {
            if (transtype[i] =='W') {
                balance = balance - transamount[i];
                System.out.println("\t" + i + "\t\t withdraw \t\t\t "+ transamount[i] + "\t\t" + balance);
            } else{
                balance = balance +transamount[i];
                System.out.println("\t" + i + "\t\t deposite \t "+ transamount[i] + "\t\t\t\t" + balance);
                }
        }
        System.out.println("=====================================================================================");
        }
}       