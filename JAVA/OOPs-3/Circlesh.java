package OOPs;

public class Circlesh extends Shapes {
    double radius = 1.0;

    public Circlesh(double radius) {
        this.radius = radius;
    }

    public double getRadius() {
        return radius;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }
    public double getArea() {
        Area = radius * radius;
    } 
    public double Perimeter() {
        Perimeter = 2 *3.142 *radius * radius;
    }
    public Circlesh () {
        
    }

    @Override
    public String toString() {
        return "Circlesh [radius=" + radius + "]";
    }
    public Circlesh(String colour, Boolean filled, double radius) {
        super(colour, filled);
        this.radius = radius;
    }
    
}
