public class Datee {

    final int[] newdays = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};    
    
    int day;
    int months;
    int year;

    public Datee(int day, int months, int year) {
        this.day = day;
        this.months = months;
        this.year = year;
    }
    public int getDay() {
        return day;
    }
    public void setDay(int day) {
        this.day = day;
    }
    public int getMonths() {
        return months;
    }
    public void setMonths(int months) {
        this.months = months;
    }
    public int getYear() {
        return year;
    }
    public void setYear(int year) {
        this.year = year;
    }
    @Override
    public String toString() {
        return "Datee [day=" + day + ", months=" + months + ", year=" + year + "]";
    }

    public Datee minus(int num) {
    int newDay = day - num;
    int newmonths = months - 1;
    while(newDay<0) {
        newDay = newDay +  newdays[newmonths];
        if(newDay<0) {
            newmonths--;
        }
    }
        return new Datee(newDay, newmonths, year);
    }
}   
   
