// https://www.codewars.com/kata/566efcfbf521a3cfd2000056
public class FunReverse {

    public static String funReverse(String s) {
        char[] result = new char[s.length()];
        for (int i = 0; i < s.length() / 2; ++i) {
            result[2 * i + 1] = s.charAt(i);
        }

        for (int i = s.length() - 1; i >= s.length() / 2; --i) {
            result[2 * (s.length() - 1 - i)] = s.charAt(i);
        }

        return new String(result);
    }
}