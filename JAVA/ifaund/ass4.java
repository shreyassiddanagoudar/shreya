import java.util.Scanner;
public class ass4 {
    
    public static void main (String[] args) {
    
        float a,b,c;
        Scanner scan = new Scanner (System.in); 
        System.out.println("Enter the values of a %f :");
        a = scan.nextFloat();
        System.out.println("Enter the values of b %f :");
        b = scan.nextFloat();
        scan.close();
        c = a+b;
        c = a-b;
        c = a*b;
        c = a/b;
        c = a%b;
         
    System.out.print ("value is " + c + "\n" );
    System.out.print ("value is " + c + "\n" );
    System.out.print ("value is " + c + "\n" );
    System.out.print ("value is " + c + "\n" );
    System.out.print ("value is " + c + "\n" );
    
    
    }
    }
