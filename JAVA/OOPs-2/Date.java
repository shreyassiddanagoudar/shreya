public class Date {
    int Day;
    int Month;
    int Year;
    public int months;
    
    
    public void setDate(int day, int month,int year) {
        this.Day = day;
        this.Month = month;
        this.Year = year;
     
    }
    public int getDay() {
        return Day;
    }
    public void setDay(int day) {
        Day = day;
    }
    public int getMonth() {
        return Month;
    }
    public void setMonth(int month) {
        Month = month;
    }
    public int getYear() {
        return Year;
    }
    public void setYear(int year) {
        Year = year;
    }
    public String toString() {
        return + Day + "/" + Month + "/" + Year ;
    }
    public Date(int day, int month, int year) {
        this.Day = day;
        this.Month = month;
        this.Year = year;
    }
}
