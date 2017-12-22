// https://www.codewars.com/kata/5679aa472b8f57fb8c000047
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Kata {

    public static int findEvenIndex(int[] arr) {
        List<Integer> list = IntStream.of(arr).boxed().collect(Collectors.toList());
        return IntStream.range(0, arr.length).filter(
                i -> ((Integer) list.subList(0, i).stream().mapToInt(y -> y).sum()).intValue()
                             == ((Integer) list.subList(i + 1, list.size()).stream().mapToInt(y -> y).sum()).intValue()
        ).findFirst().orElse(-1);
    }
}
