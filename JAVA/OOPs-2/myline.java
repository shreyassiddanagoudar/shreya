public class myline {
    Mypoint begin ;
    Mypoint end ;
    
    public Mypoint getBegin() {
        return begin;
    }
    public void setBegin(Mypoint begin) {
        this.begin = begin;
    }
    public Mypoint getEnd() {
        return end;
    }
    public void setEnd(Mypoint end) {
    this.end = end;
    }
    public Mypoint getBeginX() {
        return beginX;
    }
    public void setBeginX(Mypoint beginX) {
        this.beginX = beginX;
    }
    public Mypoint getEndY() {
        return endY;
    }
    public void setEndY(Mypoint endY) {
        this.endY = endY;
    }
    public Mypoint getBeginXY() {
        return beginXY;
    }
    public void setBeginXY(Mypoint beginXY) {
        this.beginXY = beginXY;
    }
    public Mypoint getEndXY() {
        return endXY;
    }
    public void setEndXY(Mypoint endXY) {
        this.endXY = endXY;
    }
    public double getLength() {
        return length;
    }
    
    public double getGradient() {
        return gradient;
    }
    public myline(int x1, int y1, int x2, int y2) {
        this.x1 = x1;
        this.y1 = y1;
        this.x2 = x2;
        this.y2 = y2;
    }
    public myline(Mypoint begin, Mypoint end) {
        this.begin = begin;
        this.end = end;
    }
    @Override
    public String toString() {
        return "myline [begin=" + begin + ", end=" + end + "]";
    }
    
}
