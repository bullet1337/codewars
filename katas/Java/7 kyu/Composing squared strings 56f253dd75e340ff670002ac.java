// https://www.codewars.com/kata/56f253dd75e340ff670002ac
import java.util.stream.Collectors;
import java.util.stream.IntStream;

class Composing {

    public static String compose(String s1, String s2) {
        String[] subs1 = s1.split("\n"), subs2 = s2.split("\n");

        return IntStream.range(0, subs1.length).mapToObj(i ->
            subs1[i].substring(0, i + 1) + subs2[subs2.length - 1 - i].substring(0, subs2.length - i)
        ).collect(Collectors.joining("\n"));
    }
}