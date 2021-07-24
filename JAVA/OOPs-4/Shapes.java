package OOPs;

public class Shapes {
    String colour = "red";
    Boolean filled = true;
    
    public String getColour() {
        return colour;
    }
    public void setColour(String colour) {
        this.colour = colour;
    }
    public Boolean getFilled() {
        return filled;
    }
    public void setFilled(Boolean filled) {
        this.filled = filled;
    }
    public Shapes(String colour, Boolean filled) {
        this.colour = colour;
        this.filled = filled;
    }
    public Shapes() {
        
    }

    @Override
    public String toString() {
        return "Shapes [colour=" + colour + ", filled=" + filled + "]";
    }
    
}
