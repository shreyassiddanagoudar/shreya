public class Book {
    String title;
    int isbn;
    int price;
    int bookid;
    int yearofpublication;
    double editionnumber;
    
    public String getTitle() {
        return title;
    }
    public void setTitle(String title) {
        this.title = title;
    }
    public int getIsbn() {
        return isbn;
    }
    public void setIsbn(int isbn) {
        this.isbn = isbn;
    }
    public int getPrice() {
        return price;
    }
    public void setPrice(int price) {
        this.price = price;
    }
    public int getBookid() {
        return bookid;
    }
    public void setBookid(int bookid) {
        this.bookid = bookid;
    }
    public int getYearofpublication() {
        return yearofpublication;
    }
    public void setYearofpublication(int yearofpublication) {
        this.yearofpublication = yearofpublication;
    }
    public double getEditionnumber() {
        return editionnumber;
    }
    public void setEditionnumber(double editionnumber) {
        this.editionnumber = editionnumber;
    }
    public Book(String title, int isbn, int price, int bookid, int yearofpublication, double editionnumber) {
        this.title = title;
        this.isbn = isbn;
        this.price = price;
        this.bookid = bookid;
        this.yearofpublication = yearofpublication;
        this.editionnumber = editionnumber;
    }
    @Override
    public String toString() {
        return "Book [bookid=" + bookid + ", editionnumber=" + editionnumber + ", isbn=" + isbn + ", price=" + price
                + ", title=" + title + ", yearofpublication=" + yearofpublication + "]";
    }

}
