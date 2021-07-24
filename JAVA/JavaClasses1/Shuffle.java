import java.util.ArrayList;
import java.util.Iterator;
import java.util.*;

public class Shuffle {
    public static void main(String[] args){
    
    System.out.println("======ColourList======");

    ArrayList<String> colourlist = new ArrayList<>();
    colourlist.add("white");
    colourlist.add("red");
    colourlist.add("blue");
    colourlist.add("yellow");
        Collections.shuffle(colourlist);
    System.out.println(colourlist);


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



