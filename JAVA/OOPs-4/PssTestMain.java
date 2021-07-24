public class PssTestMain {
    public static void main(String args[]) {
        Person1 p1, p2;
        Student1 s1, s2;
        Staff1 stf1, stf2;

        p1 = new Person1("Shreya", "vij");
        System.out.println(p1.toString());
       
        p2 = new Person1();
        p2.setAdress("CL");
        p2.setName("Shash");
        System.out.println(p2.toString());

        s1 = new Student1("Shreya", "vij", "abc", 1998, 35000);
        System.out.println(s1.toString());

        s2 = new Student1();
        s2.setProgram("abc");
        s2.setYear(1998);
        s2.setFee(35000);
        System.out.println(s2.toString());

        stf1 = new Staff1("klaus", "verginia", "mystic falls", 340000);
        System.out.println(stf1.toString());


    }
}
