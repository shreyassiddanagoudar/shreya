import java.lang.Thread;
public class TJthread1  {
    public static void main(String[] args) {
        // Jthread t1 = new Jthread() ;
        // t1.start();
        // Jthread t2 = new Jthread() ;
        // t2.start();
        // Thread t3 = new Thread(new JthreadR(2)) ;
        // // t3.start();
        // t3.run();
        // Thread t4 = new Thread(new JthreadR(10)) ;
        // // t4.start();
        // t4.run();

        T1 t11 = new T1();
        T2 t12 = new T2();
        T3 t13 = new T3();
        t11.start();
        t11.join() ;
        t12.start(); // t12 is not exectued till t11 comes out
        t12.join() ;
        t13.start(); // t13 is not executed till t12 comes out
    }
}