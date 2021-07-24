public class Adress {
    String add1;
    String add2;
    int cityid;
    int stateid;
    public String getAdd1() {
        return add1;
    }
    public void setAdd1(String add1) {
        this.add1 = add1;
    }
    public String getAdd2() {
        return add2;
    }
    public void setAdd2(String add2) {
        this.add2 = add2;
    }
    public int getCityid() {
        return cityid;
    }
    public void setCityid(int cityid) {
        this.cityid = cityid;
    }
    public int getStateid() {
        return stateid;
    }
    public void setStateid(int stateid) {
        this.stateid = stateid;
    }
    public Adress(String add1, String add2, int cityid, int stateid) {
        this.add1 = add1;
        this.add2 = add2;
        this.cityid = cityid;
        this.stateid = stateid;
    }
    @Override
    public String toString() {
        return "Adress [add1=" + add1 + ", add2=" + add2 + ", cityid=" + cityid + ", stateid=" + stateid + "]";
    }

}
