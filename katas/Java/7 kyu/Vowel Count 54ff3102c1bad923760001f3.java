// https://www.codewars.com/kata/54ff3102c1bad923760001f3
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Vowels {

    public static int getCount(String str) {
        int vowels = 0;
        Matcher m = Pattern.compile("[aioue]").matcher(str);

        while (m.find()) {
            ++vowels;
        }

        return vowels;
    }
}