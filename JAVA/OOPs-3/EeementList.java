import java.util.ArrayList;
import java.util.Iterator;

public class EeementList {
    public static void main(String[] args){
    
    System.out.println("======Element List======");

    ArrayList<Integer> elementlist = new ArrayList<>();
    elementlist.add(1);
    elementlist.add(2);
    elementlist.add(3);
    elementlist.add(5);

    System.out.println(elementlist);


System.out.println("======Iterator======");
Iterator<Integer> it = elementlist.iterator();

while (it.hasNext()) {
    System.out.println(it.next());
}
System.out.println("======forEach======");

elementlist.forEach((element)->{
    System.out.println(element);
});

} 

}



