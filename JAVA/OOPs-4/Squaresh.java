package OOPs;

public class Squaresh extends Shapes {
    double squaresh;
    double side;
    String colour;
    boolean filled;
    public Squaresh(String colour, Boolean filled, double squaresh, double side, String colour2, boolean filled2) {
        super(colour, filled);
        this.squaresh = squaresh;
        this.side = side;
        colour = colour2;
        filled = filled2;
    }
    public Squaresh(double squaresh, double side, String colour, boolean filled) {
        this.squaresh = squaresh;
        this.side = side;
        this.colour = colour;
        this.filled = filled;
    }
    public double getSquaresh() {
        return squaresh;
    }
    public void setSquaresh(double squaresh) {
        this.squaresh = squaresh;
    }
    public double getSide() {
        return side;
    }
    public void setSide(double side) {
        this.side = side;
    }
    public String getColour() {
        return colour;
    }
    public void setColour(String colour) {
        this.colour = colour;
    }
    public boolean isFilled() {
        return filled;
    }
    public void setFilled(boolean filled) {
        this.filled = filled;
    }
    
}
