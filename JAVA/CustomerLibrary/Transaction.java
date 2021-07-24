public class Transaction {
  int id;
  int date;
  int libraryid;
  int customerid;
  int bookid;
  String type;
public int getId() {
    return id;
}
public void setId(int id) {
    this.id = id;
}
public int getDate() {
    return date;
}
public void setDate(int date) {
    this.date = date;
}
public int getLibraryid() {
    return libraryid;
}
public void setLibraryid(int libraryid) {
    this.libraryid = libraryid;
}
public int getCustomerid() {
    return customerid;
}
public void setCustomerid(int customerid) {
    this.customerid = customerid;
}
public int getBookid() {
    return bookid;
}
public void setBookid(int bookid) {
    this.bookid = bookid;
}
public String getType() {
    return type;
}
public void setType(String type) {
    this.type = type;
}
public Transaction(int id, int date, int libraryid, int customerid, int bookid, String type) {
    this.id = id;
    this.date = date;
    this.libraryid = libraryid;
    this.customerid = customerid;
    this.bookid = bookid;
    this.type = type;
}
@Override
public String toString() {
    return "Transaction [bookid=" + bookid + ", customerid=" + customerid + ", date=" + date + ", id=" + id
            + ", libraryid=" + libraryid + ", type=" + type + "]";
}  
}
