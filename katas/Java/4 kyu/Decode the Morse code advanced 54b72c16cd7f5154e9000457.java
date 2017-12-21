// https://www.codewars.com/kata/54b72c16cd7f5154e9000457
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class MorseCodeDecoder {

    public static String decodeBits(String bits) {
        Matcher m = Pattern.compile("(0+)|(1+)").matcher(bits.replaceAll("^0+|0+$", ""));
        List<String> matches = new ArrayList<>();
        int rate = Integer.MAX_VALUE;

        while (m.find()) {
            String group = m.group();
            if (group.length() < rate) {
                rate = group.length();
            }
            matches.add(m.group());
        }

        int finalRate = rate;
        return matches.stream().map(x -> x.length() / finalRate == 1
                ? (x.charAt(0) == '0' ? "" : ".")
                : (x.length() / finalRate == 3 ? (x.charAt(0) == '0' ? " " : "-") : "   ")
        ).collect(Collectors.joining());
    }

    public static String decodeMorse(String morseCode) {
        return Stream.of(morseCode.trim().split(" {3}")).map(
                x -> Stream.of(x.split(" ")).map(y -> MorseCode.get(y)).collect(Collectors.joining())
        ).collect(Collectors.joining(" "));
    }
}