public class DiffDateeTestMain {
    
    public static void main(String[] args, int newDay) {
        DiffDatee d1= new DiffDatee(12,3,2021);
        DiffDatee  d2= new DiffDatee(23,5,2021);

        if(d1.months>d2.months) {
            int d = newDay - d1.months;
        }
        else {
            int d5 = newDay - d2.months;
        }

        System.out.println(d1.minus(newDay));
        System.out.println(d2.minus(newDay));
    }
}

