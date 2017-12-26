// https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0
import static java.lang.Math.max;
import static java.lang.Math.min;

public class RemoveChars {
    public static String remove(String str) {
      return str.substring(min(1, str.length()), max(0, str.length() - 1));
    }
}
