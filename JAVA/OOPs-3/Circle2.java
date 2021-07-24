public class Circle2 {
    double radius = 1.0;
    String color = "red";
    
    public Circle2(double radius) {
        this.radius = radius;
    }
    public Circle2(double radius, String color) {
        this.radius = radius;
        this.color = color;
    }
    public double getRadius() {
        return radius;
    }
    public void setRadius(double radius) {
        this.radius = radius;
    }
    public String getColor() {
        return color;
    }
    public void setColor(String color) {
        this.color = color;
    }
    public double getArea(){
        return 3.14*radius*radius;
    }
    public String toString() {
        return "Circle1 [color=" + color + ", radius=" + radius + "]";
    }
    public Circle2() {
    }
}
