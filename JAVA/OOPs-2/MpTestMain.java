public class MpTestMain {
    public static void main(String args[]) {
        Mpoint a1, a2;
        Movablepoint b1, b2;

        a1 = new Mpoint(1, 2);
        System.out.println(a1.toString());

        a2 = new Mpoint();
        a2.setX(4);
        a2.setY(5);
        System.out.println(a2.toString());

        b1 = new Movablepoint(6, 7);
        System.out.println(b1.toString());

        b2 = new Movablepoint();
        b2.setX(6);
        b2.setY(7);
        System.out.println(b1.toString());
    }
}
