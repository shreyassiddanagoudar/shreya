import java.util.ArrayList;
import java.util.Iterator;

public class Update {
    public static void main(String[] args){
    
    System.out.println("======ColourList======");

    ArrayList<String> colourlist = new ArrayList<>();
    colourlist.add("white");
    colourlist.add("red");
    colourlist.add("blue");
    colourlist.add("yellow");
    // colourlist.add(0, "grey");

    System.out.println(colourlist.set(2,"yellow"));


System.out.println("======Iterator======");
Iterator<String> it = colourlist.iterator();

while (it.hasNext()) {
    System.out.println(it.next());
}
System.out.println("======forEach======");

colourlist.forEach((colour)->{
    System.out.println(colour);
});

} 

}



