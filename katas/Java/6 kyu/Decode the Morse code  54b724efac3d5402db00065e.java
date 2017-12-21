// https://www.codewars.com/kata/54b724efac3d5402db00065e
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class MorseCodeDecoder {

    public static String decode(String morseCode) {
        return Stream.of(morseCode.trim().split(" {3}")).map(
                x -> Stream.of(x.split(" ")).map(y -> MorseCode.get(y)).collect(Collectors.joining())
        ).collect(Collectors.joining(" "));
    }
}