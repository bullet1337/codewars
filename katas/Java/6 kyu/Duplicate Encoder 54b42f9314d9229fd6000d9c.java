// https://www.codewars.com/kata/54b42f9314d9229fd6000d9c
import java.util.function.Function;
import java.util.stream.Collectors;

public class DuplicateEncoder {

    static String encode(String word){
        return word.toLowerCase().chars().boxed().collect(Collectors.collectingAndThen(
                Collectors.groupingBy(Function.identity(), Collectors.counting()),
                x -> word.toLowerCase().chars().mapToObj(y -> x.get(y) == 1 ? "(" : ")").collect(Collectors.joining())
        ));
    }
}
