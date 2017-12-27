// https://www.codewars.com/kata/54d496788776e49e6b00052f
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import static java.lang.Math.max;
import static java.lang.StrictMath.sqrt;

public class SumOfDivided {

    public static int[] sieve(int n) {
        int[] numbers = new int[n + 1];
        numbers[0] = numbers[1] = 1;
        for (int i = 2; i <= sqrt(n); ++i) {
            if (numbers[i] == 0) {
                for (int j = i * i; j <= n; j += i) {
                    numbers[j] = 1;
                }
            }
        }

        return IntStream.range(0, numbers.length).filter(i -> numbers[i] == 0).toArray();
    }

    public static String sumOfDivided(int[] l) {
        Arrays.sort(l);
        int[] primes = sieve(max(l[l.length - 2], l[l.length - 1] / 2));
        Map<Integer, List<Integer>> primesMap
                = IntStream.of(primes).boxed().collect(Collectors.toMap(x -> x, x -> new ArrayList<>()));
        for (int e : l) {
            for (int p : primes) {
                if (e % p == 0) {
                    primesMap.get(p).add(e);
                }
            }
        }

        return primesMap.entrySet().stream().filter(e -> !e.getValue().isEmpty()).sorted(Map.Entry.comparingByKey())
                        .map(e -> "(" + e.getKey() + " " + e.getValue().stream().mapToInt(x -> x).sum() + ")")
                        .collect(Collectors.joining());
    }
}
