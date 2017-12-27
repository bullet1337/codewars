// https://www.codewars.com/kata/54dc6f5a224c26032800005c
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class StockList {

    public static String stockSummary(String[] lstOfArt, String[] lstOf1stLetter) {
        if (lstOfArt.length == 0 || lstOf1stLetter.length == 0) {
            return "";
        }

        Map<String, Integer> codeQuantity = Stream.of(lstOfArt).collect(Collectors.groupingBy(
                s -> s.substring(0, 1), Collectors.summingInt(s -> Integer.valueOf(s.split(" ")[1])))
        );
        return Stream.of(lstOf1stLetter).map(s -> '(' + s + " : " + codeQuantity.getOrDefault(s, 0) + ")")
                     .collect(Collectors.joining(" - "));
    }
}
