// https://www.codewars.com/kata/55983863da40caa2c900004e
import java.util.Arrays;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Kata {

    public static long nextBiggerNumber(long n) {
        int[] x = String.valueOf(n).chars().toArray();
        int i;
        for (i = x.length - 1; i >= 1; --i) {
            if (x[i] > x[i - 1]) {
                break;
            }
        }

        if (i > 0) {
            int minIndex = i;
            for (int j = i + 1; j < x.length; ++j) {
                if (x[i - 1] < x[j] && x[j] < x[minIndex]) {
                    minIndex = j;
                }
            }

            int tmp = x[minIndex];
            x[minIndex] = x[i - 1];
            x[i - 1] = tmp;

            if (i < x.length) {
                Arrays.sort(x, i, x.length);
            }

            return Long.valueOf(IntStream.of(x).mapToObj(e -> String.valueOf((char) e)).collect(Collectors.joining()));
        } else {
            return -1;
        }
    }
}