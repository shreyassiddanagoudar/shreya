package OOPs;

public class Rectanglesh extends Shapes {
    double width = 1.0;
    double lenhgth = 1.0;
    
    public double getWidth() {
        return width;
    }
    public void setWidth(double width) {
        this.width = width;
    }
    public double getLenhgth() {
        return lenhgth;
    }
    public void setLenhgth(double lenhgth) {
        this.lenhgth = lenhgth;
    }
    public Rectanglesh(String colour, Boolean filled, double width, double lenhgth) {
        super(colour, filled);
        this.width = width;
        this.lenhgth = lenhgth;
    }
    public Rectanglesh(double width, double lenhgth) {
        this.width = width;
        this.lenhgth = lenhgth;
    }
    public Rectanglesh () {

    }
    @Override
    public String toString() {
        return "Rectanglesh [lenhgth=" + lenhgth + ", width=" + width + "]";
    }

    
}
