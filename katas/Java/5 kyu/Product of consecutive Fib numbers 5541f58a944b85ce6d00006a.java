// https://www.codewars.com/kata/5541f58a944b85ce6d00006a
import java.util.LinkedList;
import java.util.List;

public class ProdFib {

    public static long[] productFib(long prod) {
        List<Long> fibs = new LinkedList<>();
        fibs.add(0L);
        fibs.add(1L);
        int i = 0;
        while (fibs.get(i) * fibs.get(i + 1) < prod) {
            fibs.add(fibs.get(i) + fibs.get(i + 1));
            ++i;
        }

        return new long[]{fibs.get(i), fibs.get(i + 1), fibs.get(i) * fibs.get(i + 1) == prod ? 1 : 0};
    }
}