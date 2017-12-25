// https://www.codewars.com/kata/5629db57620258aa9d000014
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.function.Function;
import java.util.stream.Collectors;

import static java.lang.StrictMath.max;

public class Mixing {
    static Map<Integer, String> prefixes = new HashMap<>();

    static {
        prefixes.put(-1, "2:");
        prefixes.put(0, "=:");
        prefixes.put(1, "1:");
    }

    public static String mix(String s1, String s2) {
        Map<Integer, Long> charMap1 = s1.chars().boxed().filter(x -> 'a' <= x && x <= 'z')
                                        .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
        charMap1.entrySet().removeIf(e -> e.getValue() <= 1);

        Map<Integer, Long> charMap2 = s2.chars().boxed().filter(x -> 'a' <= x && x <= 'z')
                                        .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
        charMap2.entrySet().removeIf(e -> e.getValue() <= 1);

        Map<Integer, String> charString = new HashMap<>();
        for (Entry<Integer, Long> e : charMap2.entrySet()) {
            if (charMap1.containsKey(e.getKey())) {
                charMap1.merge(e.getKey(), e.getValue(), (x, y) -> {
                    charString.put(e.getKey(), prefixes.get(x.compareTo(y)));
                    return max(x, y);
                });
            } else {
                charMap1.put(e.getKey(), e.getValue());
                charString.put(e.getKey(), "2:");
            }
        }

        return charMap1.entrySet().stream()
                       .map(e -> charString.getOrDefault(e.getKey(), "1:")
                               + new String(new char[e.getValue().intValue()])
                               .replace("\0", String.valueOf((char) e.getKey().intValue())))
                       .collect(Collectors.collectingAndThen(Collectors.groupingBy(String::length, Collectors.toList()),
                                z -> z.entrySet().stream()
                                      .sorted(Entry.<Integer, List<String>>comparingByKey().reversed())
                                      .flatMap(x -> x.getValue().stream().sorted())
                                      .collect(Collectors.joining("/"))));
    }
}