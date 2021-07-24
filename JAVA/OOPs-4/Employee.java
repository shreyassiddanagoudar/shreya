
public class Employee {
    int ID;
    String firstName;
    String lastName;
    int salary;
    
    public String getName() {
        return firstName+lastName;
    }
    
    public int getID() {
        return ID;
    }
    public String getFirstName() {
        return firstName;
    }
    public String getLastName() {
        return lastName;
    }
    public int getSalary() {
        return salary;
    }
    public void setSalary(int salary) {
        this.salary = salary;
    }
    public int getAnnualSalary() {
        return salary*12;
    }
    public int raiseSalary(int percent) {
        return salary + (percent/100)*salary;
    }

    public String toString() {
        return "Employee [firstName=" + firstName + ", id=" + ID + ", lastName=" + lastName + ", salary=" + salary
                + "]";
    }
    public Employee(int id, String firstName, String lastName, int salary) {
        this.ID = id;
        this.firstName = firstName;
        this.lastName = lastName;
        this.salary = salary;
    }
}
