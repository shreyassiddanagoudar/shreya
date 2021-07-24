import java.util.Scanner;
public class ass1 {

    public static void main (String[] args) {

        int add, sub, mul, div,  mod,a,b;
        Scanner scan = new Scanner (System.in); 
        System.out.println("Enter the values of a :");
        a = scan.nextInt();
        System.out.println("Enter the values of b :");
        b = scan.nextInt();
        scan.close();
        add = a+b;
        sub = a-b;
        mul = a*b;
        div = a/b;
        mod =a%b;
         
    System.out.print ("value is " + add + "\n" );
    System.out.print ("value is " + sub + "\n" );
    System.out.print ("value is " + mul + "\n" );
    System.out.print ("value is " + div + "\n" );
    System.out.print ("value is " + mod + "\n" );
    

    }
}