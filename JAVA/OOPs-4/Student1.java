public class Student1 extends Person1 {
    String program;
    int year;
    double fee;
    public String getProgram() {
        return program;
    }
    public void setProgram(String program) {
        this.program = program;
    }
    public int getYear() {
        return year;
    }
    public void setYear(int year) {
        this.year = year;
    }
    public double getFee() {
        return fee;
    }
    public void setFee(double fee) {
        this.fee = fee;
    }
    public Student1(String name, String adress, String program, int year, double fee) {
        super(name, adress);
        this.program = program;
        this.year = year;
        this.fee = fee;
    }
    @Override
    public String toString() {
        return "Student1 [fee=" + fee + ", program=" + program + ", year=" + year + "]";
    }
    public Student1() {
    }
}
