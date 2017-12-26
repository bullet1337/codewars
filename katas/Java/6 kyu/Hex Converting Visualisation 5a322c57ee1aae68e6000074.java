// https://www.codewars.com/kata/5a322c57ee1aae68e6000074
public class Hexadecimal {
    public static String showHexConversion(int number) {
        StringBuilder s = new StringBuilder();
        int length = String.valueOf(number).length(), quotientLength = 0, n = number;
        String spaces = new String(new char[length]).replace("\0", " ");
        boolean twoDigits = false;
        while (number > 0) {
            int m = number % 16;
            twoDigits |= m >= 10;
            s.append(spaces.substring(0, spaces.length() - String.valueOf(number).length())).append(number).append('/')
             .append(16).append("=");
            number /= 16;
            if (quotientLength == 0) {
                quotientLength = String.valueOf(number).length();
            }
            s.append(spaces.substring(0, quotientLength - String.valueOf(number).length())).append(number)
             .append(" R").append(" ").append(spaces.substring(0, 2 - String.valueOf(m).length())).append(m)
             .append('\n');
        }

        spaces = s.append("Result=").append(Integer.toHexString(n).toUpperCase()).toString();
        if (!twoDigits) {
            return spaces.replaceAll("R {2}", "R ");
        } else {
            return spaces;
        }
    }
}