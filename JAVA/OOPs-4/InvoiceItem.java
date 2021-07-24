public class InvoiceItem {
    String ID;
    String Desc;
    int Qty;
    double unitPrice;

    public String getID() {
        return ID;
    }
    public void setID(String iD) {
        ID = iD;
    }
    public String getDesc() {
        return Desc;
    }
    public void setDesc(String desc) {
        Desc = desc;
    }
    public int getQty() {
        return Qty;
    }
    public void setQty(int qty) {
        Qty = qty;
    }
    public double getUnitPrice() {
        return unitPrice;
    }
    public void setUnitPrice(double unitPrice) {
        this.unitPrice = unitPrice;
    }
    public double getTotal() {
        return unitPrice;
    }
    
    public String toString() {
        return "InvoiceItem [Desc=" + Desc + ", ID=" + ID + ", Qty=" + Qty + ", unitPrice=" + unitPrice + "]";
    }
    public InvoiceItem(String iD, String desc, int qty, double unitPrice) {
        ID = iD;
        Desc = desc;
        Qty = qty;
        this.unitPrice = unitPrice;
    }
    
    
}
