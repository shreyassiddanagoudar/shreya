package OOPs;

public class Number {
   int sum, mul, div, mod, power, negative, positive, even, odd, prime;
  

   
   public static void main(String args[]) {
       Number n1 = new Number();
       n1.add(2, 3);
       n1.mul(5, 6);
       n1.div();
       n1.mod();
       n1.power();
       n1.negative();
       n1.positive();
       n1.even();
       n1.odd();
       n1.prime();
   }

   void add(int a, int b) {
    sum = a+b;
    System.out.println("Addition of two numbers =%d " + sum);
   }
   void mul(int a, int b) {
       mul=a*b;
       System.out.println("Multiplication of two numbers is =%d" +mul);
   }
   void div(int a, int b) {
        div=a/b;
        System.out.println("Div of two numbers is =%d" +div);
    }
    void mod(int a, int b) {
        mod=a%b;
        System.out.println("Modilousn of two numbers is =%d" +mod);
    }
    void power(int base, int digit) {
        power=ab;
        System.out.println("Multiplication of two numbers is =%d" +mul);
    }
}
