// https://www.codewars.com/kata/5616868c81a0f281e500005c
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

class Rank {

    public static String nthRank(String st, Integer[] we, int n) {
        if (st.length() == 0) {
            return "No participants";
        }

        if (n > we.length) {
            return "Not enough participants";
        }

        String[] names = st.split(",");

        return IntStream.range(0, names.length).boxed().collect(Collectors.collectingAndThen(
                Collectors.toMap(
                        i -> names[i],
                        i -> names[i].chars()
                                     .reduce(names[i].length(),
                                             (x, y) -> x + y + 1 - (Character.isLowerCase(y) ? 'a' : 'A'))
                                * we[i]
                ),
                e -> e.entrySet().stream()
                      .sorted(Map.Entry.<String, Integer>comparingByValue().reversed()
                                                                           .thenComparing(Map.Entry.comparingByKey()))
                      .map(Map.Entry::getKey).toArray(String[]::new)[n - 1]
        ));
    }
}