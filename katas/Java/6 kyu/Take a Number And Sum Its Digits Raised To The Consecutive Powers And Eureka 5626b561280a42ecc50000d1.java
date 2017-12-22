// https://www.codewars.com/kata/5626b561280a42ecc50000d1
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.LongStream;

import static java.lang.Math.pow;

class SumDigPower {

    public static List<Long> sumDigPow(long a, long b) {
        return LongStream.rangeClosed(a, b).boxed().filter(x -> {
            final String strX = String.valueOf(x);
            return x == IntStream.range(0, strX.length()).map(i -> (int) pow(Character.getNumericValue(strX.charAt(i)),
                                                                             i + 1)).sum();
        }).collect(Collectors.toList());
    }
}