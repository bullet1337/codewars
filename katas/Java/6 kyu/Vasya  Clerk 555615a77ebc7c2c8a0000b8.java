// https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8
import java.util.HashMap;
import java.util.Map;

public class Line {

    public static String Tickets(int[] peopleInLine) {
        int bill_50 = 0, bill_25 = 0;

        for (int e : peopleInLine) {
            switch (e) {
                case 25:
                    ++bill_25;
                    break;
                case 50:
                    if (bill_25 > 0) {
                        --bill_25;
                    } else {
                        return "NO";
                    }
                    ++bill_50;
                    break;
                case 100:
                    if (bill_25 > 0) {
                        if (bill_50 > 0) {
                            --bill_50;
                            --bill_25;
                        } else if (bill_25 >= 3) {
                            bill_25 -= 3;
                        } else {
                            return "NO";
                        }
                    } else {
                        return "NO";
                    }
            }
        }

        return "YES";
    }
}