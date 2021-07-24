import java.util.ArrayList;
import java.util.Iterator;

public class Collections {
    public static void main(String[] args){
    int a;
    a=10;
    int b=10;
    a = b+a;
    System.out.println(a);


    int[] e = {1, 2, 3, 4};
    System.out.println("======ArrayList======");
    for (int i=0; i<4; i++) {
        
        System.out.println(e[i]);
    }
    

    System.out.println("======CarList======");

    ArrayList<String> carlist = new ArrayList<>();
    carlist.add("fiat");
    carlist.add("amamba");
    carlist.add("suzur");
    carlist.add("totu");

    System.out.println(carlist);

    System.out.println("======forloop======");

    for (int i=0; i<carlist.size(); i++) {
        System.out.println(carlist.get(i));
    }
        System.out.println(carlist.size());
        System.out.println(carlist.add("fiat"));
        System.out.println(carlist.indexOf("totu"));
        System.out.println(carlist.contains(2));



System.out.println("======Iterator======");
Iterator<String> it = carlist.iterator();

while (it.hasNext()) {
    System.out.println(it.next());
}
System.out.println("======forEach======");

carlist.forEach((car)->{
    System.out.println(car);
});

}

	public static void sort(ArrayList<String> colourlist) {
	}

    public static void extract(ArrayList<String> colourlist) {
    }

   
}

    // Author[] authors =  new Author[2];
    // author[0] = new Author("Shreya", "Shreya@gmail.com", 'm');
    // author[1] = new Author("Shash", "Shash@gmail.com", 'm');

    // Genre fiction = new Genre ("Fiction", 10);
    // Genre fiction = new Genre("Non-fiction", 11);
    
    // Book dummyBook = new Book("Java for dummy", authors, 19.95,99,fiction);
    // System.out.println(dummyBook);

    // dummyBook.setPrice(29.95);
    // dummyBook.setQty(28);
    // System.out.println("name is :" + dummyBook.getName());
    // System.out.println("price is :" + dummyBook.getPrice());
    // System.out.println("qty is :" + dummyBook.getQty());
    // System.out.println("author is :" + dummyBook.getAuthor());
    // System.out.println("author's name is :" + dummyBook.getAuthor()[0].getName());
    // System.out.println("author's email name is :" + dummyBook.getAuthor()[0].getEmail());

