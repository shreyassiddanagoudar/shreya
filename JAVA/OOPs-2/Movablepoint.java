public class Movablepoint extends Mpoint {
    float xSpeed;
    float ySpeed;
    
    public float getxSpeed() {
        return xSpeed;
    }
    public void setxSpeed(float xSpeed) {
        this.xSpeed = xSpeed;
    }
    public float getySpeed() {
        return ySpeed;
    }
    public void setySpeed(float ySpeed) {
        this.ySpeed = ySpeed;
    }
    public void setSpeed(float x, float y) {
        setX(x);
        setY(y);
    }
    public float[] getSpeed() {
        float [] res = new  float [2];
        res[0] = x;
        res[1]=y;
        return res;
    }
    @Override
    public String toString() {
        return "Movablepoint [xSpeed=" + xSpeed + ", ySpeed=" + ySpeed + "]";
    }
    public Movablepoint(float x, float y, float xSpeed, float ySpeed) {
        super(x, y);
        this.xSpeed = xSpeed;
        this.ySpeed = ySpeed;
    }
    public Movablepoint(float xSpeed, float ySpeed) {
        this.xSpeed = xSpeed;
        this.ySpeed = ySpeed;
    }
    public Movablepoint() {
        float xSpeed = 0.0f;
        float ySpeed = 0.0f;
    }
    public Movablepoint move(){
        x +=xSpeed;
        y +=ySpeed;
        return this;
    }
}
