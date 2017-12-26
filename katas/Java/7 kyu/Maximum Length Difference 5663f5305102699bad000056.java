// https://www.codewars.com/kata/5663f5305102699bad000056
import java.util.stream.Stream;

import static java.lang.Math.abs;

class MaxDiffLength {

    public static int mxdiflg(String[] a1, String[] a2) {
        return Stream.of(a1).map(x -> Stream.of(a2).map(y -> abs(y.length() - x.length())).mapToInt(z -> z).max())
                     .mapToInt(w -> w.orElse(-1)).max().orElse(-1);
    }
}