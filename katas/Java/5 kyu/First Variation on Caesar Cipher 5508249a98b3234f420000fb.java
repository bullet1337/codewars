// https://www.codewars.com/kata/5508249a98b3234f420000fb
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import static java.lang.Math.floorMod;
import static java.lang.Math.min;

public class CaesarCipher {
    static List<Character> letters
            = IntStream.rangeClosed('a', 'z').mapToObj(x -> (char) x).collect(Collectors.toList());

    public static List<String> movingShift(String s, int shift) {
        int partSize = (int) Math.ceil(s.length() / 5.0);

        List<String> list = new ArrayList<>();
        for (int i = 0; i < 5; i++) {
            StringBuilder part = new StringBuilder("");
            if (i * partSize < s.length()) {
               for (char c : s.substring(i * partSize, min((i + 1) * partSize, s.length())).toCharArray()) {
                   if (Character.isLetter(c)) {
                       if (Character.isLowerCase(c)) {
                           part.append(letters.get((c - 'a' + shift++) % letters.size()));
                       } else {
                           part.append((char) (letters.get((c - 'A' + shift++) % letters.size()) + 'A' - 'a'));
                       }
                   } else {
                       part.append(c);
                       ++shift;
                   }
               }
            }

            list.add(part.toString());
        }
        return list;
    }

    public static String  demovingShift(List<String> s, int shift) {
        StringBuilder str = new StringBuilder("");
        for (char c : String.join("", s).toCharArray()) {
            if (Character.isLetter(c)) {
                if (Character.isLowerCase(c)) {
                    str.append(letters.get(floorMod(c - 'a' - shift++, letters.size())));
                } else {
                    str.append((char) (letters.get(floorMod(c - 'A' - shift++, letters.size())) + 'A' - 'a'));
                }
            } else {
                str.append(c);
                ++shift;
            }
        }

        return str.toString();
    }
}