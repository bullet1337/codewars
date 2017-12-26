// https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Accumul {

    public static String accum(String s) {
        return IntStream.range(0, s.length())
                        .mapToObj(i -> s.substring(i, i + 1).toUpperCase()
                                + new String(new char[i]).replace('\0', s.charAt(i)).toLowerCase())
                        .collect(Collectors.joining("-"));
    }
}