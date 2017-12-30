// https://www.codewars.com/kata/5a40fc7ce1ce0e34440000a3
import java.util.function.Function;
import java.util.stream.Collectors;

public class DD {

    public static boolean isDD(int n) {
        return String.valueOf(n).chars().boxed().collect(Collectors.collectingAndThen(
                Collectors.groupingBy(Function.identity(), Collectors.counting()),
                x -> x.entrySet().stream().anyMatch(e -> Character.getNumericValue(e.getKey()) == e.getValue())
        ));
    }
}
