public class BookTest {
    public static void main(String[] args) {
       // Construct an author instance
       // Author ahTeck = new Author[]("Tan Ah Teck", "ahteck@nowhere.com", 'm');
      //   System.out.println(ahTeck);  // Author's toString().
      Author[] author=new Author[2];
      author[0] = new Author("xyz", "xyz@gmail.com", 'F');
      author[1] = new Author("abc", "abc@gmail.com", 'M');


        // construct Genre
        Genre fiction = new Genre("Fiction", 10);
        Genre nonFiction = new Genre("Non Fiction", 11);
        Book1 dummyBook = new Book1("Java for dummy", author, 19.95f, 99, fiction);  // Test Book's Constructor
        System.out.println(dummyBook);  // Test Book's toString()

    

        // Test Getters and Setters
        dummyBook.setPrice(29.95f);
        dummyBook.setQty(28);
        System.out.println("name is: " + dummyBook.getName());
        System.out.println("price is: " + dummyBook.getPrice());
        System.out.println("qty is: " + dummyBook.getQty());
        System.out.println("Author is: " + dummyBook.getAuthor[]());  // Author's toString()
        System.out.println("Author's name is: " + dummyBook.getAuthor[0].getName());
        System.out.println("Author's email is: " + dummyBook.getAuthor[1].getEmail());

        // Use an anonymous instance of Author to construct a Book instance
        Book1 anotherBook = new Book1("more Java",  new Author("Paul Tan", "paul@somewhere.com", 'm'), 29.95f, nonFiction);
           // new Author("Paul Tan", "paul@somewhere.com", 'm'), 29.95f, nonFiction);
        System.out.println(anotherBook);  // toString()

    }
 }
 