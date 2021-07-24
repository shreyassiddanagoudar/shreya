import java.util.Scanner;
public class ass2 {
    
public static void main (String[] args) {

    int a,b,c;
    Scanner scan = new Scanner (System.in); 
    System.out.println("Enter the values of a :");
    a = scan.nextInt();
    System.out.println("Enter the values of b :");
    b = scan.nextInt();
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