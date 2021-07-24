public class Circle {
    int radius;
    String colour;
    static float pi= 3.142f;
    int diameter;
    float perimeter;
    float area;
    public class radius {
        this.radius = radius;
        this.colour = colour;
    }
public static void main(String args[]) {
    Circle c1 = new Circle("BLUE");
    c1.setRadius(5);
    c1.getRadius();
    c1.diameter();
    c1.perimeter();
    c1.area();

    Circle c2 = new Circle("YELLOW");
    c2.setRadius(2);
    c2.getRadius();
    c2.diameter();
    c2.perimeter();
    c2.area();
}

Circle (String c) {
    colour = c;
    System.out.println("Circle colour is " + colour);
}
void setRadius(int radius) {
    System.out.println("radius= " + radius);
}
int getRadius() {
    return this.radius;
}
int diameter() {
    return diameter = radius + radius;
}
float perimeter() {
   return 2 * pi * radius;
}

float area() {
   return pi * radius * radius;
}
public Object inttoString() {
return Circle(" Radius \t\t diameter\t\t perimeter\t\tarea");
}

private Object Circle(String string) {
    return null;
}
}
