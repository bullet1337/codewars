// https://www.codewars.com/kata/58989a079c70093f3e00008d
import java.util.stream.IntStream;

public class Kata {

    public static int[][] cartesianNeighbor(int x, int y) {
        return IntStream.rangeClosed(x - 1, x + 1).boxed()
                        .flatMap(q -> IntStream.rangeClosed(y - 1, y + 1)
                                               .mapToObj(w -> new int[]{q, w}))
                        .filter(e -> e[0] != x || e[1] != y).toArray(int[][]::new);
    }
}