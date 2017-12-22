// https://www.codewars.com/kata/5412509bd436bd33920011bc
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Maskify {

    public static String maskify(String str) {
        return str.length() > 4
                   ? IntStream.range(0, str.length() - 4).mapToObj(x -> "#").collect(Collectors.joining())
                        + str.substring(str.length() - 4)
                   : str;
    }
}
