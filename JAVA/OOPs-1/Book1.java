public class Book1 {
    String name;
    Author[] author;
    float price;
    int qty;
    Genre genre;
    public Book1(String name, Author[] author, float price, int qty, Genre genre) {
        this.name = name;
        this.author = author;
        this.price = price;
        this.qty = qty;
        this.genre = genre;
    }
    public Book1(String name, Author[] author, float price, Genre genre) {
        this.name = name;
        this.author = author;
        this.price = price;
        this.genre = genre;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public Author[] getAuthor() {
        return author;
    }
    public void setAuthor(Author[] author) {
        this.author = author;
    }
    public float getPrice() {
        return price;
    }
    public void setPrice(float price) {
        this.price = price;
    }
    public int getQty() {
        return qty;
    }
    public void setQty(int qty) {
        this.qty = qty;
    }
    public Genre getGenre() {
        return genre;
    }
    public void setGenre(Genre genre) {
        this.genre = genre;
    }
    
    public String toString() {
        return "Book1 [author=" + author + ", genre=" + genre + ", name=" + name + ", price=" + price + ", qty=" + qty
                + "]";
    }
    
}
