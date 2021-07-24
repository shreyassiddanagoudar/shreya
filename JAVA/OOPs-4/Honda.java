public class Honda extends Bike {
    void run() {
        System.out.println(Running Honda Bike!);
    }
    void anotherrun() {
        System.out.println( Another Run Honda Bike!);
    }
    void another() {
        super.another();
        System.out.println( Not an abstract method calling from Honda class!!!!);
    }
}
