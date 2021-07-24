public class Time {
    int Hour;
    int Minute;
    int Second;
   
    public void setTime(int hour, int minute, int second) {
        this.Hour = hour;
        this.Minute = minute;
        this.Second = second;
    }
      
    public int getHour() {
        return Hour;
    }
    public void setHour(int hour) {
        Hour = hour;
    }
    public int getMinute() {
        return Minute;
    }
    public void setMinute(int minute) {
        Minute = minute;
    }
    public int getSecond() {
        return Second;
    }
    public void setSecond(int second) {
        Second = second;
    }
   
    public Time nextSecond() {
        if(this.Second == 59){
            this.Second = 00;
            if(this.Minute == 59){
                this.Minute = 00;
                if(this.Hour == 59){
                    this.Hour = 23;
                }
            }

        } else{
            this.Second = Second +1;
        }
        return this;
    
    }
    public Time previousSecond() {
        if(this.Second == 00){
            this.Second = 59;
            if(this.Minute == 00){
                this.Minute = 59;
                if(this.Hour == 00){
                    this.Hour = 23;
                }
            }

        } else{
            this.Second = Second -1;
        }
    return this;
    }
    
    
    public String toString() {
        return "Time [Hour=" + Hour + ", Minute=" + Minute + ", Second=" + Second + "]";
    }
    public Time(int hour, int minute, int second) {
        this.Hour = hour;
        this.Minute = minute;
        this.Second = second;
    }
    
}
