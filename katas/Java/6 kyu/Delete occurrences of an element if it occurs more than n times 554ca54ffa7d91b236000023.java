// https://www.codewars.com/kata/554ca54ffa7d91b236000023
import java.util.*;

public class EnoughIsEnough {

    public static int[] deleteNth(int[] elements, int maxOcurrences) {
        List<Integer> result = new ArrayList<>(elements.length);
        Map<Integer, Long> counter = new HashMap<>();

        for (int e : elements) {
            if (counter.merge(e, (long) 1, (x, y) -> x + y) <= maxOcurrences) {
                result.add(e);
            }
        }

        return result.stream().mapToInt(x -> x).toArray();
    }
}