public class Mypoint {
   int x =0 ;
   int y =0;//decleration
   public Mypoint() {
    //    x = 0;
    //    y = 0;//instance variable
   }
public Mypoint(int x, int y) {
    this.x = x;
    this.y = y;//local variable
}
public int getX() {
    return x;
}
public void setX(int x) {
    this.x = x;
}
public int getY() {
    return y;
}
public void setY(int y) {
    this.y = y;
}

public void setXY(int x, int y) {
    this.x = x;
    this.y = y;
}

public int[] getXY() {
    int [] a = new int[2];
    a[0] = this.x;
    a[1] = this.y;
    return a;
}

// public String toString() {
//     return "(x,y)";
// } 
public String toString() {
    return "Mypoint [x=" + x + ", y=" + y + "]";
}

private double findDistance(int x1, int y1, int x2, int y2) {
    int xdiff = x1 - x2;
    int ydiff = y1 - y2;
    return Math.sqrt(xdiff*xdiff + ydiff* ydiff);
}
public double distance(int x, int y) {
    return findDistance(this.x, this.y, x,y);
}
public double distance () {
    return findDistance(this.x, this.y, 0, 0);

}
public double distance (Mypoint another) {
    return findDistance(this.x, this.y, another.x, another.y);

}



}
