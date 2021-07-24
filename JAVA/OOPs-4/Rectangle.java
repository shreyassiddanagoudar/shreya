public class Rectangle {
    float len = 1.0f;
    float width = 1.0f;
    
    
    public float getLen() {
        return len;
    }
    public void setLen(float len) {
        this.len = len;
    }
    public float getWidth() {
        return width;
    }
    public void setWidth(float width) {
        this.width = width;
    }
    public double getArea() {
        return 2*len*width;
    }
    public double getperimeter() {
        return len*width;
    }
    public String toString() {
        return "Rectangle [len=" + len + ", width=" + width + "]";
    }
    public Rectangle(float len, float width) {
        this.len = len;
        this.width = width;
    }
    public Rectangle() {
        this.len = len;
        this.width = width;
    }
}
