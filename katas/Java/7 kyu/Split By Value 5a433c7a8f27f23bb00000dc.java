// https://www.codewars.com/kata/5a433c7a8f27f23bb00000dc
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Solution {

    int[] splitByValue(int k, int[] elements) {
        return IntStream.of(elements).boxed().collect(Collectors.groupingBy(e -> e >= k)).entrySet().stream()
                        .sorted(Map.Entry.comparingByKey()).flatMap(e -> e.getValue().stream()).mapToInt(x -> x)
                        .toArray();
    }
}