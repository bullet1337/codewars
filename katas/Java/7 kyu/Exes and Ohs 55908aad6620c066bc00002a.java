// https://www.codewars.com/kata/55908aad6620c066bc00002a
public class XO {

    public static boolean getXO (String str) {
        return str.replaceAll("[xX]", "").length()
                       == str.replaceAll("[oO]", "").length();
    }
}