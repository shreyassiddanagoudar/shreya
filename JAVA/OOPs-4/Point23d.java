public class Point23d {
    public static void main(String args[]) {
        Point2d a1, a2;
        Point3d b1, b2, b3;

        a1 = new Point2d(1, 2);
        System.out.println(a1.toString());
        
        a2 = new Point2d();
        a2.setX(6);
        a2.setY(8);
        System.out.println(a2.toString());

        b1 = new Point3d(1, 2, 3);
        System.out.println(b1.toString());

        b2 =new Point3d();
        b2.setX(4);
        b2.setY(5);
        b2.setZ(6);
        System.out.println(b2.toString());

        b3 = new Point3d();
        b3.setX(2);
        b3.setY(6);
        b3.setZ(7);
        System.out.println(b3.toString());
    }

}
