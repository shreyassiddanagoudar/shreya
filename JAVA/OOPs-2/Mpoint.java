public class Mpoint {
    float x;
    float y;
    
    public float getX() {
        return x;
    }
    public void setX(float x) {
        this.x = x;
    }
    public float getY() {
        return y;
    }
    public void setY(float y) {
        this.y = y;
    }
    public void setXY(float x, float y) {
        setX(x);
        setY(y);
    }
    public float[] getXY() {
        float [] ans = new float [2];
        ans [0] = x;
        ans [1] = y;
        return ans;
    }  
    @Override
    public String toString() {
        return "Mpoint [x=" + x + ", y=" + y + "]";
    }
    public Mpoint(float x, float y) {
        this.x = x;
        this.y = y;
    }
    public Mpoint () {
        float x = 0.0f;
        float y = 0.0f;
    }

}