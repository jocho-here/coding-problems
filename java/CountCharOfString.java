import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

public class CountCharOfString {
  public static void main(String [] args) {

    String a = args[0];
    char[] charArry = a.toCharArray();
    HashMap<Character, Integer> hash = new HashMap<Character, Integer>();

    for(int n =0; n < charArry.length; n++) {
      if (hash.containsKey(charArry[n]))
        hash.put(charArry[n], hash.get(charArry[n])+1);
      else
        hash.put(charArry[n], 1);
    }

    Set<Map.Entry<Character, Integer>> sett = hash.entrySet();
    Iterator<Map.Entry<Character, Integer>> itr = sett.iterator();

    while(itr.hasNext()) {
      Map.Entry<Character, Integer> ent = itr.next();
      System.out.println(ent.getKey() + " " + ent.getValue());
    }
  }
}
