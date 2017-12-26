// https://www.codewars.com/kata/55084d3898b323f0aa000546
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import static java.lang.Math.floorMod;
import static java.lang.Math.min;

public class CaesarTwo {
    static List<Character> letters
            = IntStream.rangeClosed('a', 'z').mapToObj(x -> (char) x).collect(Collectors.toList());

    public static List<String> encodeStr(String s, int shift) {
        StringBuilder result = new StringBuilder("");
        for (int i = 0; i < s.length(); ++i) {
            char c = s.charAt(i);
            if (Character.isLetter(c)) {
                if (Character.isLowerCase(c)) {
                    result.append(letters.get((c - 'a' + shift) % letters.size()));
                } else {
                    result.append((char) (letters.get((c - 'A' + shift) % letters.size()) + 'A' - 'a'));
                }
            } else {
                result.append(c);
            }

            if (i == 0) {
                result.insert(0, Character.toLowerCase(c));
                result.insert(1, Character.toLowerCase(result.charAt(1)));
            }
        }


        int partSize = (int) Math.ceil(result.length() / 5.0);

        List<String> list = new ArrayList<>();
        for (int i = 0; i < 5; i++) {
            list.add(result.substring(i * partSize, min((i + 1) * partSize, result.length())));
        }
        list.removeIf(x -> x.length() == 0);

        return list;
    }

    public static String  decode(List<String> s) {
        String prefix = s.set(0, s.get(0).substring(2));
        int shift = prefix.charAt(1) - prefix.charAt(0);

        StringBuilder str = new StringBuilder("");
        for (char c : String.join("", s).toCharArray()) {
            if (Character.isLetter(c)) {
                if (Character.isLowerCase(c)) {
                    str.append(letters.get(floorMod(c - 'a' - shift, letters.size())));
                } else {
                    str.append((char) (letters.get(floorMod(c - 'A' - shift, letters.size())) + 'A' - 'a'));
                }
            } else {
                str.append(c);
            }
        }

        return str.toString();
    }
}