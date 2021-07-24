public class Point3d extends Point2d {
    float z ;

    public float getZ() {
        return z;
    }

    public void setZ(float z) {
        this.z = z;
    }
    public void setXYZ(float x, float y, float z) {
        setX(x);
        setY(y);
        setZ(z);
    }
    public float[] getXYZ() {
        float [] ans = new float [3];
        ans[0] = x;
        ans[1] = y;
        ans[2] = z;
        return ans;
    }

    @Override
    public String toString() {
        return "Point3d [z=" + z + "]";
    }
    public Point3d(float x, float y, float z) {
        super(x, y);
        this.z = z;
    }

    public Point3d() {
        float z = 0.0f;
    }

    
}
