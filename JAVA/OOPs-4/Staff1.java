public class Staff1 extends Person1 {
    String school;
    double pay;
    public String getSchool() {
        return school;
    }
    public void setSchool(String school) {
        this.school = school;
    }
    public double getPay() {
        return pay;
    }
    public void setPay(double pay) {
        this.pay = pay;
    }
    public Staff1(String name, String adress, String school, double pay) {
        super(name, adress);
        this.school = school;
        this.pay = pay;
    }
    
    @Override
    public String toString() {
        return "Staff1 [pay=" + pay + ", school=" + school + "]";
    }
}
