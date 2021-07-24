import java.lang.Math;
public class TryMonth { //class or templets
    int date;
    int day;
    int month;
    final int[] daysInMonth ={31,28,31,30,31,30,31,31,30,31,30,31 };
    final String [] dayName = {"friday", "saturday", "sunday", "monday", "tuesday", "wednesday", "thursday"};
    public TryMonth(int date, int day, int month) {
        this.date = date;
        this.day = day;
        this.month = month;
    }
    public int getDate() {
        return date;
    }
    public void setDate(int date) {
        this.date = date;
    }
    public int getDay() {
        return day;
    }
    public void setDay(int day) {
        this.day = day;
    }
    public int getMonth() {
        return month;
    }
    public void setMonth(int month) {
        this.month = month;
    }
    public TryMonth() {

    }
    @Override
    public String toString() {
        return "TryMonth [date=" + date + ", day=" + day + ", month=" + month + "]";
    }
    public int getDiff (TryMonth d2) {
        int diff = 0;
        if(this.month == d2.month && this.day ==d2.day) {
            return diff;
        }
        else if(this.month == d2.month) {
            diff = Math.abs(this.day=d2.day); 
        }
        else {
            int smallMonth = this.month < d2.month ? this.month:d2.month;
            int smallDay = this.month < d2.month ? this.month:d2.day;
            int largeMonth = this.month > d2.month ? this.month:d2.month;
            int largeDay = this.month > d2.month ? this.month:d2.day;

            for(int i=smallMonth; i<largeMonth; i++) {
                if(i == smallMonth) {
                    diff = daysInMonth[i-1] - smallDay;
                }
                else {
                    diff = diff + daysInMonth[i-1];
                }
                return diff + largeDay;
            }
        }
    }
    public String getDayName(TryMonth d) {
        int diff = this.getDiff(d);
        System.out.println(diff);
        int dayNum = diff % 7;
        return dayName[dayNum];
    }
    
}
